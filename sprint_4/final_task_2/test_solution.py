import random
from collections import Counter

import pytest

from sprint_4.final_task_2.solution import (
    LinkedList,
    MyReinventedTable,
    jenkins_int32_hash,
)


def test_put_get_single():
    ll = LinkedList()
    ll.put("a", 1)

    assert ll.get("a") == 1
    assert ll.get("b") is None


def test_put_overwrite_value():
    ll = LinkedList()
    ll.put("a", 1)
    ll.put("a", 2)

    assert ll.get("a") == 2


def test_put_creates_chain():
    ll = LinkedList()
    ll.put("a", 1)
    ll.put("b", 2)
    ll.put("c", 3)

    # вставляем в голову, но логика доступа по ключам должна работать
    assert ll.get("a") == 1
    assert ll.get("b") == 2
    assert ll.get("c") == 3


def test_remove_existing_head():
    ll = LinkedList()
    ll.put("a", 1)
    ll.put("b", 2)  # станет головой

    retval = ll.remove("b")
    assert retval is not None
    assert retval == 2

    assert ll.get("b") is None
    assert ll.get("a") == 1


def test_remove_existing_middle():
    ll = LinkedList()
    ll.put("a", 1)
    ll.put("b", 2)
    ll.put("c", 3)

    # сейчас голова "c" -> "b" -> "a"
    retval = ll.remove("b")
    assert retval is not None
    assert retval == 2
    assert ll.get("b") is None
    assert ll.get("a") == 1
    assert ll.get("c") == 3


def test_remove_non_existing():
    ll = LinkedList()
    ll.put("a", 1)

    assert ll.remove("b") is None
    assert ll.get("a") == 1


@pytest.mark.parametrize(
    "pairs, lookup_key, expected_value",
    [
        ([], "x", None),
        ([("a", 1)], "a", 1),
        ([("a", 1)], "b", None),
        ([("a", 1), ("b", 2), ("c", 3)], "b", 2),
        ([("a", 1), ("b", 2), ("c", 3)], "z", None),
    ],
)
def test_get_parametrized(pairs, lookup_key, expected_value):
    ll = LinkedList()
    for k, v in pairs:
        ll.put(k, v)

    assert ll.get(lookup_key) == expected_value


@pytest.mark.parametrize(
    "initial_pairs, key_to_remove, removed, remaining_keys",
    [
        ([("a", 1)], "a", True, []),
        ([("a", 1), ("b", 2)], "a", True, ["b"]),
        ([("a", 1), ("b", 2)], "b", True, ["a"]),
        ([("a", 1), ("b", 2)], "x", False, ["a", "b"]),
        ([("a", 1), ("b", 2), ("c", 3)], "b", True, ["a", "c"]),
    ],
)
def test_remove_parametrized(initial_pairs, key_to_remove, removed, remaining_keys):
    ll = LinkedList()
    for k, v in initial_pairs:
        ll.put(k, v)

    result = True if ll.remove(key_to_remove) is not None else False

    assert result is removed

    for key in remaining_keys:
        assert ll.get(key) is not None

    # убедимся, что удалённого ключа точно нет
    assert ll.get(key_to_remove) is None


# ---------- Тесты jenkins_int32_hash ----------
def test_jenkins_hash_is_deterministic():
    keys = [-(10**9), -1, 0, 1, 10**9]
    for k in keys:
        h0 = jenkins_int32_hash(k)
        for _ in range(100):
            assert jenkins_int32_hash(k) == h0


def test_jenkins_hash_returns_uint32_range():
    # несколько характерных значений, включая отрицательные
    keys = [0, 1, -1, 123, -123, 10**9, -(10**9)]
    for k in keys:
        h = jenkins_int32_hash(k)
        assert isinstance(h, int)
        assert 0 <= h <= 0xFFFFFFFF


def test_jenkins_hash_same_bits_same_hash():
    # числа, различающиеся на 2**32, должны давать одинаковый результат
    base = 123456789
    for delta in (-1, 0, 1):
        k = base + delta
        h1 = jenkins_int32_hash(k)
        h2 = jenkins_int32_hash(k + (1 << 32))
        assert h1 == h2


def test_jenkins_hash_avalanche_small_delta_changes_hash():
    # близкие по значению ключи должны давать сильно разные хеши
    k1 = 1000
    k2 = 1001
    h1 = jenkins_int32_hash(k1)
    h2 = jenkins_int32_hash(k2)
    # не равны
    assert h1 != h2
    # и отличаются по битам существенно (эвристика)
    diff_bits = bin(h1 ^ h2).count("1")
    assert diff_bits > 8  # чисто эвристический порог


# ---------- Тесты _get_bucket_index ----------
def test_bucket_index_is_deterministic():
    table = MyReinventedTable()

    keys = [-(10**9), -123, 0, 123, 10**9]

    for k in keys:
        idx_first = table._get_bucket_index(k)
        for _ in range(100):
            assert table._get_bucket_index(k) == idx_first


def test_bucket_index_in_range():
    table = MyReinventedTable()
    keys = [-(10**9), -123, 0, 123, 10**9]
    for k in keys:
        idx = table._get_bucket_index(k)
        assert 0 <= idx < table._TABLE_SIZE


def test_bucket_index_same_bits_same_index():
    table = MyReinventedTable()
    for k in range(-1000, 1001):
        idx1 = table._get_bucket_index(k)
        idx2 = table._get_bucket_index(k + (1 << 32))
        assert idx1 == idx2


def test_bucket_index_distribution_smoke():
    """
    Небольшая проверка равномерности распределения индексов.
    Не строгий статистический тест, а smoke-test.
    """
    table = MyReinventedTable()
    buckets = table._TABLE_SIZE

    num_keys = 50_000
    counter = Counter()

    rng = random.Random(123456)
    for _ in range(num_keys):
        k = rng.randint(-(10**9), 10**9)
        idx = table._get_bucket_index(k)
        counter[idx] += 1

    # не должно быть индексов вне диапазона
    assert all(0 <= i < buckets for i in counter.keys())

    if counter:
        loads = list(counter.values())
        max_load = max(loads)
        # при N < M многие корзины будут пустыми, но max_load должен быть мал
        # это простой sanity-check, а не строгая гарантия
        assert max_load < 10


# ---------- Базовые интеграционные тесты MyReinventedTable ----------


def test_table_put_get_single():
    table = MyReinventedTable()
    table.put(0, 1)

    assert table.get(0) == 1
    assert table.get(1) is None


def test_table_put_overwrite_value():
    table = MyReinventedTable()
    table.put(1000000, 1)
    table.put(1000000, 2)

    assert table.get(1000000) == 2


def test_table_put_multiple_and_get():
    table = MyReinventedTable()
    pairs = [(-101, 1), (101, 2), (0, 3)]
    for k, v in pairs:
        table.put(k, v)

    for k, v in pairs:
        assert table.get(k) == v
    assert table.get(1) is None


def test_table_remove_existing_keys():
    table = MyReinventedTable()
    table.put(-1000000000, 1)
    table.put(1000000000, 2)
    table.put(0, 3)

    retval = table.remove(1000000000)
    assert retval is not None
    assert retval == 2
    assert table.get(1000000000) is None
    assert table.get(-1000000000) == 1
    assert table.get(0) == 3


def test_table_remove_non_existing_key():
    table = MyReinventedTable()
    table.put(777, 777)

    assert table.remove(0) is None
    assert table.get(777) == 777


@pytest.mark.parametrize(
    "pairs, lookup_key, expected_value",
    [
        ([], 15, None),
        ([(99999999, 1)], 99999999, 1),
        ([(-151233123, 5555555)], 17, None),
        ([(-1234, 1), (0, 2), (1234, 3)], 1234, 3),
        ([(555, 1), (666, 2), (777, 3)], 888, None),
    ],
)
def test_table_get_parametrized(pairs, lookup_key, expected_value):
    table = MyReinventedTable()
    for k, v in pairs:
        table.put(k, v)

    assert table.get(lookup_key) == expected_value
