from ahmed_menu.src.ahmed_menu.menu import menu
from io import StringIO
import pytest


def funca():
    return 'I am funca'


def funcb():
    return 'I am funcb'


@pytest.mark.parametrize('choice,output', [
    ('a', 'I am funca'),
    ('b', 'I am funcb')
])
def test_choices(monkeypatch, capsys, choice, output):
    monkeypatch.setattr('sys.stdin', StringIO(f'{choice}\n'))
    result = menu(a=funca, b=funcb)

    assert result == output


def test_bad_choice(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('c\na\n'))
    result = menu(a=funca, b=funcb)
    captured_out, captured_err = capsys.readouterr()

    assert "'c' not found" in captured_out.rstrip()
    assert result == "I am funca"
