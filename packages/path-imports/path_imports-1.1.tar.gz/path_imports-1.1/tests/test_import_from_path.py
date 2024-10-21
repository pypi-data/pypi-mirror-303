from pyfakefs.fake_filesystem import FakeFilesystem

from path_imports import import_from_path


def test_py_file(fs: FakeFilesystem):
    fs.create_file("foo/bar.py", contents="x = 123")

    module = import_from_path("foo/bar.py", force_reimport=True)

    assert module.__name__ == "bar"
    assert module.x == 123


def test_package(fs: FakeFilesystem):
    fs.create_file("foo/bar/__init__.py", contents="x = 123")

    module = import_from_path("foo/bar", force_reimport=True)

    assert module.__name__ == "bar"
    assert module.x == 123
