"""
Augment sales data with lab results, licensees, inventories, inventory types, 
and strains data.
Copyright (c) 2022 Cannlytics

Authors: Keegan Skeate <keegan@cannlytics.com>
Created: 1/29/2022
Updated: 1/29/2022
License: MIT License <https://opensource.org/licenses/MIT>

Description: This script calculates various statistics from the sales data using
relevant fields from the lab results, licensees, inventories,
inventory types, and strains datasets with the lab results data.

Data sources:

    - WA State Traceability Data January 2018 - November 2021
    https://lcb.app.box.com/s/e89t59s0yb558tjoncjsid710oirqbgd?page=1
    https://lcb.app.box.com/s/e89t59s0yb558tjoncjsid710oirqbgd?page=2

Data Guide:

    - Washington State Leaf Data Systems Guide
    https://lcb.wa.gov/sites/default/files/publications/Marijuana/traceability/WALeafDataSystems_UserManual_v1.37.5_AddendumC_LicenseeUser.pdf

Data available at:

    - https://cannlytics.com/data/market/augmented-washington-state-sales
"""
# Standard imports.
import gc
import json

# External imports.
import pandas as pd

#------------------------------------------------------------------------------
# Read sales data.
#------------------------------------------------------------------------------

def read_sales(
        columns=None,
        fields=None,
        date_columns=None,
        nrows=None,
        data_dir='../.datasets',
):
    """
    1. Read Leaf lab results.
    2. Sort the data, removing null observations.
    3. Define a lab ID for each observation and remove attested lab results.
    """
    raise NotImplementedError
    # shards = []
    # lab_datasets = ['LabResults_0', 'LabResults_1', 'LabResults_2']
    # for dataset in lab_datasets:
    #     lab_data = pd.read_csv(
    #         f'{data_dir}/{dataset}.csv',
    #         sep='\t',
    #         encoding='utf-16',
    #         usecols=columns,
    #         dtype=fields,
    #         parse_dates=date_columns,
    #         nrows=nrows,
    #     )
    #     shards.append(lab_data)
    #     del lab_data
    #     gc.collect()
    # data = pd.concat(shards)
    # del shards
    # gc.collect()
    # data.dropna(subset=['global_id'], inplace=True)
    # # data.set_index('global_id', inplace=True)
    # data.sort_index(inplace=True)
    # data['lab_id'] = data['global_id'].map(lambda x: x[x.find('WAL'):x.find('.')])
    # data = data.loc[data.lab_id != '']
    # return data


#------------------------------------------------------------------------------
# Calculate sales statistics.
#------------------------------------------------------------------------------

# TODO: Aggregate total_transaction, total_revenue, and average_price
# for each lab result.

# Calculate total sales by day.
# - Is there a day of the week effect?
