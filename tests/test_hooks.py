import pytest

from requests import sessions


def hook(value):
    return value[1:]


@pytest.mark.parametrize(
    "hooks_list, result",
    (
        (hook, "ata"),
        ([hook, lambda x: None, hook], "ta"),
    ),
)
def test_hooks(hooks_list, result):
    assert sessions.dispatch_hook("response", {"response": hooks_list}, "Data") == result


def test_default_hooks():
    assert sessions.default_hooks() == {"response": []}
