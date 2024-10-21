import pytest

from pyfakefs.fake_filesystem import PatchMode
from pyfakefs.fake_filesystem_unittest import Patcher


# Per default, importing from the fake file system doesn't work. So we must define a custom fixture
# which enables that.
@pytest.fixture
def fs():
    with Patcher(patch_open_code=PatchMode.AUTO) as p:
        yield p.fs
