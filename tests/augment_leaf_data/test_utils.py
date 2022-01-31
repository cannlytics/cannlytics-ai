"""
Test Leaf Data Augmentation Utility Functions
Copyright (c) 2022 Cannlytics

Author: Keegan Skeate <keegan@cannlytics.com>
Created: 1/30/2022
Updated: 1/30/2022
License: MIT License <https://github.com/cannlytics/cannlytics-ai/blob/main/LICENSE>
"""
# External imports.
import pandas as pd
import pytest

# Internal import.
import sys
sys.path.append('../../')
sys.path.append('./')
from ai.augment_leaf_data import utils


def test_end_of_month():
    """Test the end of month utility function."""
    value = utils.end_of_month(pd.to_datetime('2021-04-20'))
    assert value == '2021-04-30'
    value = utils.end_of_month(pd.to_datetime('2021-10-20'))
    assert value == '2021-10-31'


def test_end_of_year():
    """Test the end of year utility function."""
    value = utils.end_of_year(pd.to_datetime('2021-04-20'))
    assert value == '2021-12-31'


def test_end_of_period_timeseries():
    """Test the end of year utility function."""
    value = utils.end_of_period_timeseries(
        pd.DataFrame.from_dict({
            pd.to_datetime('2021-04-01'): [1, 2],
            pd.to_datetime('2021-05-01'): [3, 4]
        }, orient='index')
    )
    assert list(value.index)[0] == pd.to_datetime('2021-04-30')
    assert list(value.index)[-1] == pd.to_datetime('2021-05-31')


def test_format_billions():
    """Test format billions."""
    value = utils.format_billions(3_600_000_000)
    assert value == '3.6B'


def test_format_millions():
    """Test format millions."""
    value = utils.format_millions(7_200_000)
    assert value == '7.2M'


def test_format_thousands():
    """Test format millions."""
    value = utils.format_thousands(4_000)
    assert value == '4K'


#FIXME:
# utils.get_number_of_lines('LICENSE')


def test_reverse_dataframe():
    """Test the end of year utility function."""
    value = utils.reverse_dataframe(
        pd.DataFrame.from_dict({
            pd.to_datetime('2021-05-01'): [3, 4],
            pd.to_datetime('2021-04-01'): [1, 2],
        }, orient='index')
    )
    assert list(value.index)[0] == pd.to_datetime('2021-04-30')
    assert list(value.index)[-1] == pd.to_datetime('2021-05-31')


def test_set_training_period():
    """Test set training period."""
    raise NotImplementedError
    # TODO: utils.set_training_period()


def test_sorted_nicely():
    """Test set training period."""
    raise NotImplementedError
    # TODO: utils.sorted_nicely()


if __name__ == '__main__':

    test_end_of_month()
    test_end_of_year()
    test_end_of_period_timeseries()
    test_format_billions()
    test_format_millions()
    test_format_thousands()
    test_reverse_dataframe()
    test_set_training_period()
    test_sorted_nicely()
    print('All Utility checks passed.')

