"""
Augment sales data with lab results, licensees, inventories, inventory types, 
and strains data.
Copyright (c) 2022 Cannlytics

Authors: Keegan Skeate <keegan@cannlytics.com>
Created: 1/29/2022
Updated: 1/30/2022
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

from ai.augment_leaf_data.utils import get_number_of_lines


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
# Read sales data.
#------------------------------------------------------------------------------

sales_datasets = ['Sales_0.csv', 'Sales_1.csv', 'Sales_2.csv']
sale_items_datasets = ['SaleItems_0.csv', 'SaleItems_1.csv', 'SaleItems_2.csv', 'SaleItems_3.csv']

# Read sales observations.
sales_fields = {
    'global_id': 'string',
    'external_id': 'string',
    'type': 'string', # wholesale or retail_recrational
    'price_total': 'float',
    'status': 'string',
    'mme_id': 'string',
    'user_id': 'string',
    'area_id': 'string',
    'sold_by_user_id': 'string',
}
sales_date_fields = [
    'created_at',
    'updated_at',
    'sold_at',
    'deleted_at',
]
sales = pd.read_csv(
    f'D:/leaf-data/Sales_0.csv',
    sep='\t',
    encoding='utf-16',
    usecols=list(sales_fields.keys()) + sales_date_fields,
    dtype=sales_fields,
    parse_dates=sales_date_fields,
    nrows=1000,
)

# Read sales items.
sales_items_fields = {
    'global_id': 'string',
    'mme_id': 'string',
    'user_id': 'string',
    'sale_id': 'string',
    'batch_id': 'string',
    'inventory_id': 'string',
    'external_id': 'string',
    'qty': 'float',
    'uom': 'string',
    'unit_price': 'float',
    'price_total': 'float',
    'name': 'string',
}
sales_items_date_fields = [
    'created_at',
    'updated_at',
    'sold_at',
    'use_by_date',
]
sale_items = pd.read_csv(
    'D:/leaf-data/SaleItems_0.csv',
    sep='\t',
    encoding='utf-16',
    usecols=list(sales_items_fields.keys()) + sales_items_date_fields,
    dtype=sales_items_fields,
    parse_dates=sales_items_date_fields,
    nrows=1000,
)


#------------------------------------------------------------------------------
# Augment sales data with licensee data.
#------------------------------------------------------------------------------

# Merge licensee_id to mme_id,.


#------------------------------------------------------------------------------
# Augment sales data with sales items data.
# Merge sales_items sale_id to sales global_id.
#------------------------------------------------------------------------------

# sales = pd.read_csv('../.datasets/augmented_sales.csv')
# sales_items_fields = {
#     'global_id': 'string',
#     'name': 'string',
# }
# sales_items_columns = list(sales_items_fields.keys())
# sales_items = pd.read_csv(
#     '../.datasets/sales_items.csv',
#     sep='\t',
#     encoding='utf-16',
#     dtype=sales_items_fields,
#     usecols=sales_items_columns,
# )
# sales_items.rename(columns={
#     'global_id': 'sales_items_id',
#     'name': 'sales_items_name',
# }, inplace=True)
# results_with_ids = pd.merge(
#     left=sales,
#     right=sales_items,
#     how='left',
#     left_on='sales_id',
#     right_on='sales_id',
# )
# results_with_ids.rename(columns={'global_id_x': 'global_id'}, inplace=True)
# results_with_ids.drop(['global_id_y'], axis=1, inplace=True, errors='ignore')
# results_with_ids.to_csv('../.datasets/augmented_sales.csv')

#------------------------------------------------------------------------------
# Augment sales data with inventories data.
#------------------------------------------------------------------------------

# Merge inventory_id to inventory_id,.

# inventories = pd.read_csv(
#     'D:/leaf-data/Inventories_0.csv',
#     sep='\t',
#     encoding='utf-16',
#     # usecols=list(sales_items_fields.keys()) + sales_items_date_fields,
#     # dtype=sales_items_fields,
#     # parse_dates=sales_items_date_fields,
#     nrows=1000,
# )

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
datatypes = {
    'lab_result_id': 'string',
    'intermediate_type': 'category',
    'status': 'category',
    'global_for_inventory_id': 'string',
    'inventory_type_id': 'string',
    'lab_id': 'string',
    'strain_id': 'string',
    'inventory_name': 'string',
    'strain_name': 'string',
    'code': 'string',
    'mme_id': 'string',
    'license_created_at': 'string',
    'name': 'string',
    'address1': 'string',
    'address2': 'string',
    'city': 'string',
    'state_code': 'string',
    'postal_code': 'string',
    'license_type': 'string',
    'cannabinoid_status': 'category',
    'cannabinoid_cbc_percent': 'float16',
    'cannabinoid_cbc_mg_g': 'float16',
    'cannabinoid_cbd_percent': 'float16',
    'cannabinoid_cbd_mg_g': 'float16',
    'cannabinoid_cbda_percent': 'float16',
    'cannabinoid_cbda_mg_g': 'float16',
    'cannabinoid_cbdv_percent': 'float16',
    'cannabinoid_cbg_percent': 'float16',
    'cannabinoid_cbg_mg_g': 'float16',
    'cannabinoid_cbga_percent': 'float16',
    'cannabinoid_cbga_mg_g': 'float16',
    'cannabinoid_cbn_percent': 'float16',
    'cannabinoid_cbn_mg_g': 'float16',
    'cannabinoid_d8_thc_percent': 'float16',
    'cannabinoid_d8_thc_mg_g': 'float16',
    'cannabinoid_d9_thca_percent': 'float16',
    'cannabinoid_d9_thca_mg_g': 'float16',
    'cannabinoid_d9_thc_percent': 'float16',
    'cannabinoid_d9_thc_mg_g': 'float16',
    'cannabinoid_thcv_percent': 'float16',
    'cannabinoid_thcv_mg_g': 'float16',
    # 'solvent_status': 'category',
    # 'solvent_acetone_ppm': 'float16',
    # 'solvent_benzene_ppm': 'float16',
    # 'solvent_butanes_ppm': 'float16',
    # 'solvent_chloroform_ppm': 'float16',
    # 'solvent_cyclohexane_ppm': 'float16',
    # 'solvent_dichloromethane_ppm': 'float16',
    # 'solvent_ethyl_acetate_ppm': 'float16',
    # 'solvent_heptane_ppm': 'float16',
    # 'solvent_hexanes_ppm': 'float16',
    # 'solvent_isopropanol_ppm': 'float16',
    # 'solvent_methanol_ppm': 'float16',
    # 'solvent_pentanes_ppm': 'float16',
    # 'solvent_propane_ppm': 'float16',
    # 'solvent_toluene_ppm': 'float16',
    # 'solvent_xylene_ppm': 'float16',
    # 'foreign_matter': 'bool',
    # 'foreign_matter_stems': 'float16',
    # 'foreign_matter_seeds': 'float16',
    # 'microbial_status': 'category',
    # 'microbial_bile_tolerant_cfu_g': 'float16',
    # 'microbial_pathogenic_e_coli_cfu_g': 'float16',
    # 'microbial_salmonella_cfu_g': 'float16',
    # 'moisture_content_percent': 'float16',
    # 'moisture_content_water_activity_rate': 'float16',
    # 'mycotoxin_status': 'category',
    # 'mycotoxin_aflatoxins_ppb': 'float16',
    # 'mycotoxin_ochratoxin_ppb': 'float16',
    # 'thc_percent': 'float16',
    # 'notes': 'float32',
    # 'testing_status': 'category',
    # 'type': 'category',
    # 'external_id': 'string',
}
date_columns = ['created_at']
columns = list(datatypes.keys()) + date_columns
results = pd.read_csv(
    'D:/leaf-data/lab_results_complete.csv',
    index_col='lab_result_id',
    dtype=datatypes,
    usecols=columns,
    parse_dates=date_columns,
)

# TODO: Calculate total cannabinoids.


inventories_size = get_number_of_lines('D:/leaf-data/Inventories_0.csv')

# TODO: Iterate over sales items.
daily_data = {}
for index, row in sale_items.iterrows():

    # For each sale item at the price_total to the day's total_sales
    # using the created_at timestamp.

    # TODO: Match with inventories,
    # reading in inventories chunk by chunk until matched
    inventory_data = None
    while not inventories or row <= inventories_size 
        inventories = pd.read_csv(
            'D:/leaf-data/Inventories_0.csv',
            sep='\t',
            encoding='utf-16',
            # usecols=list(sales_items_fields.keys()) + sales_items_date_fields,
            # dtype=sales_items_fields,
            # parse_dates=sales_items_date_fields,
            nrows=1000,
        )

    # Get lab_result_id

    # Lookup the augmented lab_result_id by lab_result_id
    lab_result = results.loc[
        results['global_for_inventory_id'] == row['inventory_id']
    ]

    # TODO: Lookup inventory_type_id, strain_id if the
    # inventory type is not yet identified.

    date = row['created_at'][:10]
    day_data = daily_data.get(date, {
        'total_sales': 0,
        'observations': 0,
        'shelf_lives': []
    })
    day_data['total_sales'] += row['price_total']
    day_data['observations'] += 1
    # TODO: Calculate time between tested and sold (shelf-life).

    # TODO: Keep track of that intermediate_type sales

    # TODO: Keep track of total_cannabinoids, lab_result_id, and total_price



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

