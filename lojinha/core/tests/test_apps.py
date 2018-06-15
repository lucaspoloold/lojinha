from lojinha.core.apps import CoreConfig


def test_name():
    assert CoreConfig.name == 'lojinha.core'
