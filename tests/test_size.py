import subprocess, sys, os


def test_runs_and_prints_header():
    """Smoke test: script runs and prints the table header line."""
    result = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), '..', 'size.py')], capture_output=True, text=True, check=True)
    stdout = result.stdout.splitlines()
    # Ensure at least 2 lines: header + separator
    assert any(line.startswith('Package') and 'Size (MB)' in line for line in stdout), 'Header line missing'
    assert any(set(line) == {'-'} and len(line) >= 10 for line in stdout), 'Separator line missing'
