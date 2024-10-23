import pytest
from click.testing import CliRunner
from et_engine_cli.filesystems import commands as fs


@pytest.fixture
def runner():
    return CliRunner()


class TestFsCommands:

    def test_list_filesystems(self, runner):
        result = runner.invoke(fs.list)
        assert result.exit_code == 0

