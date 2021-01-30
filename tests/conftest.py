import pytest

import diffy


@pytest.fixture
def cache_clear():
    diffy._diffy.cache_clear()
