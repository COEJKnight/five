import pytest
from datetime import date

from model_mommy import mommy

from usaspending_api.awards.v2.filters.award import award_filter


@pytest.fixture
def awards_data(db):
    transactions = [mommy.make('awards.TransactionNormalized', action_date=date(2014, 7, 1)),
                    mommy.make('awards.TransactionNormalized', action_date=date(2015, 7, 1)),
                    mommy.make('awards.TransactionNormalized', action_date=date(2016, 7, 1)),
                    mommy.make('awards.TransactionNormalized', action_date=date(2017, 7, 1))]

    mommy.make(
        'awards.Award',
        piid='zzz',
        fain='abc123',
        category='contract',
        type='B',
        period_of_performance_start_date=date(2014, 7, 1),
        period_of_performance_current_end_date=date(2014, 8, 1),
        total_obligation=1000,
        latest_transaction=transactions[0])
    mommy.make(
        'awards.Award',
        piid='###',
        fain='ABC789',
        category='contract',
        type='B',
        period_of_performance_start_date=date(2015, 7, 1),
        period_of_performance_current_end_date=date(2015, 8, 1),
        total_obligation=1000,
        latest_transaction=transactions[1])
    mommy.make(
        'awards.Award',
        fain='XYZ789',
        category='contract',
        type='C',
        total_obligation=1000,
        period_of_performance_start_date=date(2016, 7, 1),
        period_of_performance_current_end_date=date(2016, 8, 1),
        latest_transaction=transactions[2])
    mommy.make(
        'awards.Award',
        fain='d1e1f1',
        category='contract',
        type='C',
        total_obligation=5000,
        period_of_performance_start_date=date(2017, 7, 1),
        period_of_performance_current_end_date=date(2017, 8, 1),
        latest_transaction=transactions[3])


def test_blank_filter_returns_all(client, awards_data):
    """Test empty filter."""

    result = award_filter({})
    assert result.count() == 4


def test_filter_time_period(client, awards_data):
    """Test filtering for time period."""

    # narrow filter, gets none
    result = award_filter({
        'time_period': [{
            'start_date': '2016-01-01',
            'end_date': '2016-02-01'
        }, ]
    })
    assert result.count() == 0

    # broad filter, gets all
    result = award_filter({
        'time_period': [{
            'start_date': '2010-01-01',
            'end_date': '2020-02-01'
        }, ]
    })
    assert result.count() == 4

    # two windows, one unbounded
    result = award_filter({
        'time_period': [{
            'start_date': '2015-01-01',
            'end_date': '2016-01-01'
        }, {
            'start_date': '2017-01-01'
        }]
    })
    assert result.count() == 2
