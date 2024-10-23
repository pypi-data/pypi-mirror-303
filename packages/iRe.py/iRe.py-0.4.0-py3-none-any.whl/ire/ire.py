from dataclasses import dataclass
from inspect import getfullargspec
import os
from os import environ as env, getcwd, makedirs, rename
from os.path import islink, join, exists
from tempfile import TemporaryDirectory
from typing import Literal, Optional, Union, TypeVar, Callable, Type

import pandas as pd
from IPython.display import display, HTML, Image
from utz import err

from ire.dvc import DvcConfig, is_dvc_repo, process_dvc_config
from ire.git import GitConfig, has_unpushed_commits, process_git_config, git_staged_paths
from ire.utils import md5_file, run


DEFAULT_ARTIFACTS_DIR = ".ire"
METADATA_KEY = 'iRe'
IRE_NO_PUSH = 'IRE_NO_PUSH'
IRE_NO_GIT_PUSH = 'IRE_NO_GIT_PUSH'
IRE_NO_DVC_PUSH = 'IRE_NO_DVC_PUSH'
DEFAULT_TABLE = 'table'

TableEngine = Literal['sqlite', 'fastparquet', 'pyarrow', 'auto'] | None
ColFmts = dict[str | Type, str]
Align = Literal['left', 'center', 'right']
ColAligns = dict[str, Align]
ShowPlot = Union[None, 'png', 'html']
Fmt = Literal['parquet', 'sqlite', 'plotly', 'png']
PARQUET: Literal['parquet'] = 'parquet'
SQLITE: Literal['sqlite'] = 'sqlite'
PLOTLY: Literal['plotly'] = 'plotly'
PNG: Literal['png'] = 'png'


@dataclass
class Config:
    git: GitConfig
    dvc: DvcConfig
    dir: str = DEFAULT_ARTIFACTS_DIR
    relpath: str | None = None
    engine: TableEngine = None
    align: Align | None = None,
    show: ShowPlot = None


# Default config values
config = Config(
    git='add',
    dvc='add' if is_dvc_repo() else False,
    dir=env.get('IRE_DIR', DEFAULT_ARTIFACTS_DIR),
    relpath=env.get('IRE_RELPATH'),
    engine=env.get('IRE_ENGINE'),
    align=env.get('IRE_ALIGN'),
    show=env.get('IRE_SHOW'),
)


@dataclass
class Output:
    path: str
    md5: str


T = TypeVar("T")
DEFAULT_EXTENSION_OVERRIDES = {
    'plotly': 'json',
    'sqlite': 'db',
}


def chdir(path):
    os.chdir(path)
    config.dir = join(path, DEFAULT_ARTIFACTS_DIR)


def write_obj(
    obj: T,
    write: Callable,
    fmt: Fmt,
    name: str = None,
    dir: str = DEFAULT_ARTIFACTS_DIR,
    relpath: str = None,
    extension: str = None,
    git: GitConfig | None = None,
    dvc: DvcConfig | None = None,
    id: str | None = None,
    verbose: bool = False,
    **kwargs,
):
    if extension is None:
        extension = DEFAULT_EXTENSION_OVERRIDES.get(fmt, fmt)

    def pre_write(path: str):
        if dvc and islink(path):
            # If the file is a symlink, we need to unprotect it before writing
            run('dvc', 'unprotect', path, verbose=verbose)

    write_kwargs = {}
    extra_metadata = {}
    spec = getfullargspec(write)
    for k, v in kwargs.items():
        if k in spec.args and v is not None:
            write_kwargs[k] = v

    if name is None:
        with TemporaryDirectory(dir=getcwd()) as tmpdir:
            basename = f"tmp.{extension}"
            tmp_path = os.path.join(tmpdir, basename)
            write_rv = write(obj, tmp_path, **write_kwargs)
            md5 = md5_file(tmp_path)
            path = os.path.join(dir, f"{md5}.{extension}")
            makedirs(dir, exist_ok=True)
            pre_write(path)
            rename(tmp_path, path)
    else:
        path = os.path.join(dir, f"{name}.{extension}")
        makedirs(dir, exist_ok=True)
        pre_write(path)
        write_rv = write(obj, path, **write_kwargs)
    err(f"Saved {fmt} to {path}")
    staged_paths = git_staged_paths()
    path = process_dvc_config(dvc, path, verbose=verbose) or path
    md_path = join(relpath, path) if relpath else path
    process_git_config(git, path, verbose=verbose, staged_paths=staged_paths)
    if write_rv:
        extra_metadata.update(write_rv['metadata'])
    if id:
        extra_metadata['id'] = id
    metadata = { METADATA_KEY: { 'fmt': fmt, 'path': md_path, 'dvc': bool(dvc), **extra_metadata } }
    return metadata


def write_table(
    df: pd.DataFrame,
    path: str,
    engine: TableEngine = None,
    table: str | None = None,
    index: bool | None = None,
    fmts: ColFmts | None = None,
    align: ColAligns | None = None,
    per_page: int | None = None,
    per_page_opts: list[int] | None = None,
    verbose: bool = False,
    idx: list[str] | None = None,
    fts: list[str] | None = None,
):
    if engine is None:
        engine = 'auto'
    elif engine not in ('sqlite', 'fastparquet', 'pyarrow'):
        raise ValueError(f"Unrecognized Parquet engine: {engine}")
    metadata = dict()
    index_names = list(filter(None, df.index.names))
    if index is not False:
        if index_names:
            metadata['index'] = index_names
    if fmts:
        cols = {}
        dtypes = {}
        for col, fmt in fmts.items():
            if isinstance(col, str):
                cols[col] = fmt
            elif col is int:
                dtypes['INT'] = fmt
            elif col is float:
                dtypes['FLOAT'] = fmt
            else:
                raise ValueError(f"Unrecognized column type: {col}")
        fmts_obj = {}
        if cols:
            fmts_obj['cols'] = cols
        if dtypes:
            fmts_obj['dtypes'] = dtypes
        metadata['fmts'] = fmts_obj
    if align:
        metadata['align'] = align
    if per_page is not None:
        metadata['per_page'] = per_page
    if per_page_opts is not None:
        metadata['per_page_opts'] = per_page_opts
    metadata['count'] = len(df)
    if engine == 'sqlite':
        uri = f"sqlite:///{path}"
        metadata['table'] = table
        if exists(path):
            os.remove(path)
        df.to_sql(table, uri, index=bool(index_names) if index is None else index)
        cols = index_names + df.columns.tolist()
        # Create a SQLite connection to the table we just wrote, and execute CREATE INDEX on each column
        # to speed up queries in the iRe web app
        import sqlite3
        conn = sqlite3.connect(path)
        c = conn.cursor()
        def execute(query):
            if verbose:
                err(f"Executing: {query}")
            c.execute(query)

        idx_cols = cols if idx is None else idx
        for col in idx_cols:
            execute(f'CREATE INDEX "idx_{col}" ON "{table}" ("{col}")')

        if fts is None:
            fts_cols = []
            if df.index.dtype == 'object':
                if df.index.name:
                    fts_cols = [df.index.name]
                else:
                    err("No `index.name`; will be excluded from full text search index")
            fts_cols += [ col for col in df if df[col].dtype == 'object' ]
        else:
            fts_cols = fts
        for col in fts_cols:
            # Add a "full text search" index on all columns
            # columns_str = '", "'.join(cols)
            fts_tbl = f'{col}_fts'
            execute(f'CREATE VIRTUAL TABLE "{fts_tbl}" USING fts5("{col}", tokenize="trigram")')
            execute(f'INSERT INTO "{fts_tbl}" SELECT "{col}" FROM "{table}"')

        conn.commit()
        conn.close()
    else:
        df.to_parquet(path, engine=engine, index=bool(index_names) if index is None else index)
    return dict(metadata=metadata)


def write_image(img: Union[Image, bytes], path: str):
    with open(path, 'wb') as f:
        data = img.data if isinstance(img, Image) else img
        f.write(data)


def write_plotly(fig: 'Figure', path: str):
    fig_json = fig.to_json()
    with open(path, 'w') as f:
        f.write(fig_json)


def write_matplotlib(fig: 'plt.Figure', path: str):
    fig.savefig(path)


def maybe_handle_plotly(obj, kwargs, show: ShowPlot = None):
    try:
        from plotly.graph_objs import Figure
        if isinstance(obj, Figure):
            fig = obj
            metadata = write_obj(fig, write=write_plotly, fmt=PLOTLY, **kwargs)
            if show == 'png':
                img_bytes = fig.to_image(format='png')
                display(Image(img_bytes), metadata=metadata)
            elif show == 'html':
                html = fig.to_html()
                display(HTML(html), metadata=metadata)
            else:
                display(fig, metadata=metadata)
            return True
    except ImportError:
        pass
    return False


def maybe_handle_matplotlib(obj, kwargs):
    try:
        import matplotlib.pyplot as plt
        if isinstance(obj, plt.Figure):
            fig = obj
            metadata = write_obj(fig, write=write_matplotlib, fmt=PNG, **kwargs)
            display(fig, metadata=metadata)
            plt.close()
            return True
    except ImportError:
        pass
    return False


def export(
    obj,
    name: str = None,
    dir: str = None,
    relpath: str = None,
    git: GitConfig | None = None,
    dvc: DvcConfig | None = None,
    id: str | None = None,
    verbose: bool = False,
    show: ShowPlot = None,
    # Table kwargs
    engine: TableEngine = None,
    table: str | None = None,
    index: bool | None = None,
    fmts: ColFmts | None = None,
    align: ColAligns | None = None,
    per_page: int | None = None,
    per_page_opts: list[int] | None = None,
    idx: list[str] | None = None,
    fts: list[str] | None = None,
):
    """Export a DataFrame, Image, or Plotly figure to disk, optionally committing to Git and/or DVC.

    Args:
        obj: The object to export. DataFrame ⟹ Parquet, Image ⟹ PNG, Plotly ⟹ JSON.
        name: basename of the file to write. If not provided, a name will be generated from the MD5 hash of the object.
        dir: directory in which to write the file. If not provided, the default directory will be used.
        relpath: relative path from output notebook location to `dir`, e.g. `..` if Papermill writes an output notebook
            into a subdirectory (relative to the input notebook path). In such a case, the iRe artifacts may be written
            to `.iRe/` under the parent directory, meaning the output notebook needs to prepend a `../` tp reach them.
        git: Git configuration. If `True`, the file will be added to the Git index. If `'commit'`, the file will be
            added to the index and committed. If `'commit!'`, the file will be added to the index and committed even if
            there are existing staged changes. If `None`, the default Git configuration will be used.
        dvc: DVC configuration. If `True`, the file will be added to the DVC cache. If `'commit'`, the file will be
            added to the cache and committed. If `'commit!'`, the file will be added to the cache and committed even if
            there are existing staged changes. If `None`, the default DVC configuration will be used.
        id: ID to embed in the output metadata, which iRe/www will turn into an HTML "id" attribute (useful for
            direct-linking to a cell in a rendered "report" view of a notebook).
        verbose: Whether to print verbose output.
        show: Whether to display the exported object. If `'png'`, a PNG image will be displayed; if `'html'`, an HTML
            representation will be displayed. If `None`, the object will not be displayed.
        engine: The ``TableEngine`` ("sqlite", "fastparquet", "pyarrow", or "auto" to use when writing a DataFrame. If
            ``None``, the default ``config.engine`` will be used.
        index: Whether to include the DataFrame index when writing to Parquet. If `None`, the index will be included if
            present.
        fmts: Column formatting info to include in the output metadata; string keys are column names, `Type`s are dtypes
            (e.g. `str`, `float` to set a fallback format for all columns of that type).
        align: Column alignment overrides: [column] -> {'left', 'center', 'right'}
        per_page: Number of rows per page to display, in the iRe web app
        per_page_opts: "Rows per page" dropdown options to expose in the iRe web app
    """
    if git is None:
        git = config.git
    if dvc is None:
        dvc = config.dvc
    if dir is None:
        dir = config.dir
    if relpath is None:
        relpath = config.relpath
    if align is None:
        align = config.align
    if show is None:
        show = config.show
    if show:
        if show not in ['html', 'png']:
            raise ValueError(f"Unrecognized `show` param: {show}")

    if table is not None:
        if engine is None:
            engine = 'sqlite'
        elif engine != 'sqlite':
            raise ValueError("Cannot specify `table` with `engine` other than 'sqlite'")
    elif engine is None:
        engine = config.engine

    if engine == 'sqlite':
        if table is None:
            table = DEFAULT_TABLE

    kwargs = dict(
        dir=dir,
        relpath=relpath,
        name=name,
        git=git,
        dvc=dvc,
        id=id,
        verbose=verbose,
    )
    if isinstance(obj, pd.DataFrame):
        df = obj
        if engine == 'sqlite':
            fmt = SQLITE
        else:
            fmt = PARQUET
        kwargs.update(
            fmt=fmt,
            engine=engine,
            table=table,
            index=index,
            fmts=fmts,
            align=align,
            per_page=per_page,
            per_page_opts=per_page_opts,
            idx=idx,
            fts=fts,
        )
        metadata = write_obj(obj=obj, write=write_table, **kwargs)
        html = df._repr_html_()
        return display(HTML(html), metadata=metadata)
    elif isinstance(obj, Image):
        metadata = write_obj(obj=obj, write=write_image, fmt=PNG, **kwargs)
        return display(obj, metadata=metadata)
    elif isinstance(obj, bytes):
        img = Image(obj)
        metadata = write_obj(obj=img, write=write_image, fmt=PNG, **kwargs)
        return display(img, metadata=metadata)
    elif not maybe_handle_plotly(obj, kwargs, show=show) and not maybe_handle_matplotlib(obj, kwargs):
        raise ValueError(f"Unrecognized export type: {type(obj)}")


def _ire_df_repr_html_(df):
    return export(df)


def push(
        git: bool = True,
        dvc: Optional[bool] = None,
        # Err on the side of letting the user know about Git/DVC pushes
        verbose: bool = True,
):
    no_push = bool(env.get(IRE_NO_PUSH))
    no_git_push = bool(env.get(IRE_NO_GIT_PUSH)) or no_push
    no_dvc_push = bool(env.get(IRE_NO_DVC_PUSH)) or no_push
    if git:
        if has_unpushed_commits():
            if no_git_push:
                err(f"Git appears to have unpushed commits, but skipping push due to ${IRE_NO_PUSH if no_push else IRE_NO_GIT_PUSH}")
            else:
                run('git', 'push', verbose=verbose)
        else:
            if verbose:
                err("Git appears up to date, skipped push")
    if dvc or (dvc is None and config.dvc is not False):
        if no_dvc_push:
            err(f"DVC push skipped due to ${IRE_NO_PUSH if no_push else IRE_NO_DVC_PUSH}")
        else:
            run('dvc', 'push', verbose=verbose)
