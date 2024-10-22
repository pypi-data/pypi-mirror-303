import subprocess
import os


def capture(command):
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    return out, err, proc.returncode


def test_sum_correct():
    out, err, code = capture(["python3", "sum.py", "-n", "1", "2", "3"])
    assert err == b""
    assert out == b"6\n"
    assert code == 0


def test_square():
    out, err, code = capture(["python3", "sum.py", "-n", "1", "2", "3", "-s"])
    assert err == b""
    assert out == b"36\n"
    assert code == 0


def test_error():
    out, err, code = capture(["python3", "sum.py"])
    assert err != b""
    assert out == b""
    assert code > 0


def test_default():
    out, err, code = capture(["python3", "sum.py", "-n", "1", "5", "10", "-d", "-20"])
    assert err == b""
    assert out == b"-4\n"
    assert code == 0

def test_list_default():
    out, err, code = capture(["python3", "list_sum.py"])
    assert err == b""
    assert out == b"6\n"
    assert code == 0