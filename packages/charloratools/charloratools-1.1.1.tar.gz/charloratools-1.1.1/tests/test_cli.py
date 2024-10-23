import charloratools as clt
from pytest import LogCaptureFixture


def test_cli(caplog: LogCaptureFixture) -> None:
    """
    Tests the command line utility of installing
    torch by checking if the log outputs match
    those of a sucessful run (either torch is
    already installed or it was installed.)

    Parameters
    ----------
    caplog : LogCaptureFixture
        Pytest's built in fixture to capture and
        control logging output.
    """
    caplog.set_level("INFO")
    clt.cli.run_install_script()
    found_torch = ("Found torch" in ''.join(caplog.messages))
    installed_torch = ("Completed" in ''.join(caplog.messages))
    assert found_torch or installed_torch
