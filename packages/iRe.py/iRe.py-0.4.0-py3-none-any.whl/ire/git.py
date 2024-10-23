from dataclasses import dataclass
from typing import Optional, Union, Literal

from utz import err, check, process

from ire.utils import run


def git_has_staged_changes():
    return not check('git', 'diff', '--cached', '--quiet', 'HEAD', log=None)


def git_staged_paths():
    return process.lines('git', 'diff', '--cached', '--name-only', 'HEAD', log=None)


def git_root():
    return process.line('git', 'rev-parse', '--show-toplevel', log=None)


def current_sha():
    return process.line('git', 'rev-parse', '--short', 'HEAD', log=None)


def tracking_sha():
    return process.line('git', 'rev-parse', '--short', '@{u}', log=None)


def has_unpushed_commits():
    return current_sha() != tracking_sha()


@dataclass
class CommitConfig:
    allow_existing_staged_changes: bool = False
    verbose: bool = False

    def __call__(self, path, staged_paths: list[str] | None = None):
        self.commit(path, staged_paths=staged_paths)

    def commit(self, path, staged_paths: list[str] | None = None):
        if self.allow_existing_staged_changes or not (git_has_staged_changes() if staged_paths is None else bool(staged_paths)):
            run('git', 'add', '-f', path, verbose=self.verbose)
            if git_has_staged_changes():
                run('git', 'commit', '-m', f'iRe: add {path}', verbose=self.verbose)
            else:
                err(f"iRe: {path} appears unchanged, `git add` had no effect")
        else:
            raise RuntimeError(
                "Refusing to Git commit given existing staged changes; pass `git=commit!` to add this table to existing staged changes, and commit)"
            )


@dataclass
class PushConfig:
    commit: Optional[CommitConfig] = None
    remote: Optional[str] = None
    verbose: bool = False

    def push(self):
        remote = self.remote
        run(['git', 'push'] + [ remote ] if remote else [], verbose=self.verbose)


GitConfig = Union[
    Literal['add', 'commit', 'commit!', 'push'],
    CommitConfig,
    PushConfig,
]


def process_git_config(
        git: Optional[GitConfig],
        path: str,
        verbose: bool = False,
        staged_paths: list[str] | None = None,
):
    """Process the git config: add, commit, or push the file `path`."""
    git_configs = {
        'commit': CommitConfig(verbose=verbose),
        'commit!': CommitConfig(allow_existing_staged_changes=True, verbose=verbose),
        'push': PushConfig(commit=CommitConfig(verbose=verbose), verbose=verbose),
        'push!': PushConfig(commit=CommitConfig(allow_existing_staged_changes=True, verbose=verbose), verbose=verbose),
    }
    if isinstance(git, str) and git in git_configs:
        git = git_configs[git]
    if git == 'add':
        run('git', 'add', '-f', path, verbose=verbose)
    elif isinstance(git, CommitConfig):
        git.commit(path, staged_paths=staged_paths)
    elif isinstance(git, PushConfig):
        git.commit(path, staged_paths=staged_paths)
        run('git', 'push', verbose=verbose)
