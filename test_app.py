import subprocess
import sys

from app import main


def test_main_prints_expected_message(capsys):
    """The app should print the required CI message."""
    main()
    captured = capsys.readouterr()
    assert "Cloud CI Pipeline Running" in captured.out


def test_app_runs_without_error():
    """Running app.py as a script should exit cleanly (return code 0)."""
    result = subprocess.run(
        [sys.executable, "app.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Cloud CI Pipeline Running" in result.stdout

#done with this task