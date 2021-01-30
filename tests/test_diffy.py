import diffy


def test_diffy_0_0_0_0(cache_clear):
    assert diffy.diffy((0, 0, 0, 0)) == 1


def test_diffy_1_1_1_1(cache_clear):
    assert diffy.diffy((1, 1, 1, 1)) == 2


def test_diffy_1_9_12_3(cache_clear):
    assert diffy.diffy((1, 9, 12, 3)) == 5


def test_cache_used(cache_clear):
    diffy.diffy((0, 0, 0, 0))
    diffy.diffy((1, 1, 1, 1))
    assert diffy._diffy.cache_info().hits > 0


def test_canon(cache_clear):
    assert diffy._canon([0, 0, 1, 1]) == diffy._canon([0, 1, 1, 0])
    assert diffy._canon([0, 0, 1, 1]) != diffy._canon([0, 1, 0, 1])
    assert diffy._canon([0, 1, 2, 3]) == diffy._canon([3, 2, 1, 0])
    assert diffy._canon([0, 1, 2, 3]) != diffy._canon([0, 3, 1, 2])
