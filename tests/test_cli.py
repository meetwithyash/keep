from importlib import metadata

from click.testing import CliRunner

from keep.cli.cli import cli


def test_sanity():
    # Sanity test
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert result.output.startswith("Usage: cli [OPTIONS] COMMAND [ARGS]")


def test_version():
    # Test version
    runner = CliRunner()
    result = runner.invoke(cli, ["version"])
    assert result.exit_code == 0
    assert result.output.strip() == metadata.version("keep")


def test_run():
    # Test run
    runner = CliRunner()
    result = runner.invoke(cli, ["run", "--help"])
    assert result.exit_code == 0
    assert result.output.startswith("Usage: cli run [OPTIONS]")


def test_run_with_alerts_file():
    # Test run with alerts file
    runner = CliRunner()
    result = runner.invoke(
        cli, ["run", "--alerts-file", "tests/alerts/logfile_example.yml"]
    )
    assert result.exit_code == 0
