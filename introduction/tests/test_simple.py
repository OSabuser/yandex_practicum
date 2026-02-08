import pytest


def add(a, b):
    return a + b


def test_list_diff():
    assert [1, 2, 3] == [1, 2, 4]  # покажет diff, что отличается последний элемент


def test_str_diff():
    assert "hello\nworld" == "hello\nWorld"  # построчный дифф с подсветкой


def test_math():
    assert add(2, 3) == 4, "WTF!"


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 2),
        (2, 5, 7),
        (-1, 1, 0),
    ],
)
def test_add(a, b, expected):
    assert a + b == expected


def idfn(v):
    if isinstance(v, int):
        return f"vid={v}"
    if isinstance(v, dict):
        return f'{v["name"]}:{v["role"]}'
    return repr(v)


@pytest.mark.parametrize(
    "val",
    [
        1,
        4094,
        {"name": "alice", "role": "admin"},
    ],
    ids=idfn,
)
def test_example(val):
    assert val is not None


# В pytest есть несколько удобных способов сделать "перебор всех значений".
# Для этого необходимо указать несколько параметров parametrize
@pytest.mark.parametrize("num1", [1, 2, 3])
@pytest.mark.parametrize("num2", [4, 5, 6])
def test_service(num1, num2):
    assert num1 + num2 == num1 + num2
