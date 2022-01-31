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
# Augment sales data with licensee data.
#------------------------------------------------------------------------------

# Merge licensee_id to mme_id,.


#------------------------------------------------------------------------------
# Augment sales data with sales items data.
# Merge sales_id to sale_id.
#------------------------------------------------------------------------------

sales = pd.read_csv('../.datasets/augmented_sales.csv')
sales_items_fields = {
    'global_id': 'string',
    'name': 'string',
}
sales_items_columns = list(sales_items_fields.keys())
sales_items = pd.read_csv(
    '../.datasets/sales_items.csv',
    sep='\t',
    encoding='utf-16',
    dtype=sales_items_fields,
    usecols=sales_items_columns,
)
sales_items.rename(columns={
    'global_id': 'sales_items_id',
    'name': 'sales_items_name',
}, inplace=True)
results_with_ids = pd.merge(
    left=sales,
    right=sales_items,
    how='left',
    left_on='sales_id',
    right_on='sales_id',
)
results_with_ids.rename(columns={'global_id_x': 'global_id'}, inplace=True)
results_with_ids.drop(['global_id_y'], axis=1, inplace=True, errors='ignore')
results_with_ids.to_csv('../.datasets/augmented_sales.csv')

#------------------------------------------------------------------------------
# Augment sales data with inventories data.
#------------------------------------------------------------------------------

# Merge inventory_id to inventory_id,.

#------------------------------------------------------------------------------
# Augment sales data with inventory type data.
#------------------------------------------------------------------------------

# Merge inventory_type_id to inventory_type_id,.


#------------------------------------------------------------------------------
# Augment sales data with lab results data.
#------------------------------------------------------------------------------

# Merge lab_result_id to lab_result_id.


#------------------------------------------------------------------------------
# Calculate sales statistics.
#------------------------------------------------------------------------------

# TODO: Aggregate total_transaction, total_revenue, and average_price
# for each lab result.

# Calculate total sales by day.
# - Is there a day of the week effect?

# What is the total amount of cannabinoids consumed in Washington Sate over time?
# In mg/g, assuming dumptrucks of 100% cannabinoid concentrate, then how many
# dumptrucks a year are Washingtonians consuming?


# Answer the age old questions, does THC matter?
# If so, then how much?

# My hypothesis is that there is a direct linear relationship between THC
# concentration demanded by people and its price.

# Y-Axis Avg. price per mg/g of THC (of goods with THC)
# X-Axis g of THC produced

# Similarly
# Y-Axis Ag price per mg/g of CBD (of goods with CBD)
# X-Axis g of CBD produced

# Estimate an inverse demand function
# price_thc = y_0 + b_0 quantity_thc + u_t


# Estimate a regression of price on total_cannabinoids ***

