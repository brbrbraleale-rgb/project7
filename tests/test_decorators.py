import pytest
from decorators import log


def test_log_success(get_log):
    @log()
    def add(x, y): return x + y

    add(1, 2)
    assert get_log() == "add ok"


def test_log_error(get_log):
    @log()
    def div(x, y): return x / y

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    output = get_log()
    assert "div error: ZeroDivisionError" in output
    assert "Inputs: (1, 0), {}" in output
