import pytest

from lojinha.django_assertions import dj_assert_contains


def test_status_code(client):
    response = client.get('/contato/')
    assert 200 == response.status_code


@pytest.mark.parametrize("content", [
    "lucaspolo@lucaspolo.com.br",
    "Tel: (11) 1234-5678",
])
def test_home(client, content):
    response = client.get('/contato/')
    dj_assert_contains(response, content)
