import hashlib
import shlex
from subprocess import Popen, PIPE
import sys

from IPython import extract_module_locals


def md5_file(fname):
    """Compute the MD5 hash of a file's contents

    https://stackoverflow.com/a/3431838
    """
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def cur_cell_code(depth=0):
    lcls = extract_module_locals(depth=depth)[1]
    keys = list(lcls.keys())
    print(f"{keys=}")
    return lcls[keys[-1]]


def run(*cmd, verbose: bool = False):
    """Run a command, capturing stdout/stderr, printing iff `verbose` or a failure occurs."""
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    cmd_str = shlex.join(cmd)

    def print_streams():
        nonlocal stdout, stderr
        if stdout:
            # For some reason `dvc push` stdout sometimes comes back as b'Everything is up to date.\x1b[0m'.
            # TODO: debug (possibly login shell interference?)
            ansi_suffix = b'\x1b[0m'
            if stdout.endswith(ansi_suffix):
                stdout = stdout[:-len(ansi_suffix)]
            try:
                stdout = stdout.decode()
            except UnicodeDecodeError:
                pass
            sys.stdout.write(f'{cmd_str}: {stdout}')
        if stderr:
            try:
                stderr = stderr.decode()
            except UnicodeDecodeError:
                pass
            sys.stderr.write(f'{cmd_str}: {stderr}')

    if proc.returncode != 0:
        print_streams()
        raise RuntimeError(f"{cmd_str} failed ({proc.returncode}): {stderr}")
    elif verbose:
        print_streams()
