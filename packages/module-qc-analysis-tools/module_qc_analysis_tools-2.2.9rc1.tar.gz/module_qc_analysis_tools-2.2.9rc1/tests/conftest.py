import pathlib

import pytest
from setuptools._distutils import dir_util


@pytest.fixture()
def datadir(tmp_path, request):
    """
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    """
    # this gets the module name (e.g. /path/to/module-qc-analysis-tools/tests/test_cli.py)
    # and then gets the directory by removing the suffix (e.g. /path/to/module-qc-analysis-tools/tests/test_cli)
    test_dir = pathlib.Path(request.module.__file__).with_suffix("")

    if test_dir.is_dir():
        dir_util.copy_tree(test_dir, str(tmp_path))
        # shutil is nicer, but doesn't work: https://bugs.python.org/issue20849
        # Once pyhf is Python 3.8+ only then the below can be used.
        # shutil.copytree(test_dir, tmp_path)

    return tmp_path
