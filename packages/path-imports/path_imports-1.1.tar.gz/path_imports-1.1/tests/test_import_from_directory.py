from pyfakefs.fake_filesystem import FakeFilesystem

from path_imports import import_from_directory


def test_py_file(fs: FakeFilesystem):
    fs.create_file("foo/bar.py", contents="x = 123")

    module = import_from_directory("bar", "foo/", force_reimport=True)

    assert module.__name__ == "bar"
    assert module.x == 123
