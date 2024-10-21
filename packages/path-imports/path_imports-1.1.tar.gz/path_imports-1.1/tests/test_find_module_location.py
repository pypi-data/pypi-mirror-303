import sys
from pathlib import Path

from pyfakefs.fake_filesystem import FakeFilesystem

from path_imports import find_module_location


def test_py_file(fs: FakeFilesystem):
    fs.create_file("foo/bar.py")

    assert find_module_location("bar", directory="foo") == Path("foo/bar.py")


def test_package(fs: FakeFilesystem):
    fs.create_file("foo/bar/__init__.py")

    assert find_module_location("bar", directory="foo") == Path("foo/bar")


def test_submodule(fs: FakeFilesystem):
    fs.create_file("foo/bar/__init__.py")
    fs.create_file("foo/bar/my_module.py")

    assert find_module_location("bar.my_module", directory="foo") == Path("foo/bar/my_module.py")


def test_no_specific_directory(fs: FakeFilesystem):
    fs.create_file("foo/dummy.py")
    fs.create_file("bar/my_module.py")

    extra_paths = ["foo", "bar"]
    sys.path = extra_paths + sys.path

    try:
        assert find_module_location("my_module") == Path("bar/my_module.py")
    finally:
        del sys.path[: len(extra_paths)]
