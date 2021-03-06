import json

import pytest
from model_mommy import mommy
from rest_framework import status


from usaspending_api.references.models import Definition
from usaspending_api.common.tests.autocomplete import check_autocomplete


@pytest.fixture
def glossary_data(db):
    mommy.make(
        Definition,
        term='Word',
        plain='Plaintext response.',
        official='Official language.')
    mommy.make(
        Definition,
        term='Word2',
        plain='Plaintext response. 2',
        official='Official language. 2')
    mommy.make(
        Definition,
        term='Word3',
        plain='Plaintext response. 3',
        official='Official language. 3')


@pytest.mark.parametrize("fields,value,expected", [
    (['term'], 'Word2', {
        'term': 'Word2',
        'plain': 'Plaintext response. 2',
        'official': 'Official language. 2'
    }),
])
@pytest.mark.django_db
def test_glossary_autocomplete(client, glossary_data, fields, value, expected):
    """test partial-text search on awards."""

    check_autocomplete('references/glossary', client, fields, value, expected)


@pytest.mark.django_db
def test_bad_glossary_autocomplete_request(client):
    """Verify error on bad autocomplete request for awards."""

    resp = client.post(
        '/api/v1/references/glossary/autocomplete/',
        content_type='application/json',
        data=json.dumps({}))
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
