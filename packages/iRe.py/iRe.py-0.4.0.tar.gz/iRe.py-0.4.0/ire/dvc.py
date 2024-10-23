from os.path import join, exists
from subprocess import CalledProcessError
from typing import Optional, Union

from .git import git_root
from .utils import run


def is_dvc_repo():
    try:
        git = git_root()
    except CalledProcessError:
        return False
    dvc_dir = join(git, '.dvc')
    return exists(dvc_dir)


# True ⟹ "add"
DvcConfig = Union[bool, 'add', 'push']


def process_dvc_config(dvc: Optional[DvcConfig], path: str, verbose: bool = False):
    """Process the dvc config, returning the path to the dvc file if it was created."""
    def run_dvc(cmd):
        run('dvc', cmd, path, verbose=verbose)

    if dvc:
        run_dvc('add')
        dvc_path = f'{path}.dvc'
        if dvc == 'push':
            run_dvc('push')
        return dvc_path
    return None
