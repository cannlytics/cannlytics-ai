# Washington State Traceability Data Guide

| Data Guide | | 
|---|-----|
| Authors | Keegan Skeate <keegan@cannlytics.com> |
| Created | 2022-02-05 |
| Updated | 2022-02-05 |

The following are variable definitions for the open Washington State cannabis traceability data for the time period of approximately March 2018 to November 2021. The main datasets are as follows:

- [Licensees](#licensees)
- [Lab Results](#lab-results)
- [Inventories and Inventory Types](#inventory)
- [Strains](#strains)
- [Sales and Sale Items](#sales)
- [Batches](#batches)
- [Areas](#areas)
- [Inventory Transfers and Inventory Transfer Items](#transfers)
- [Disposals](#disposals)
- [Inventory Adjustments](#adjustments)
- [Plants](#plants)

## Licensees Data <a id="licensees" name="licensees"></a>

| Data File |  |
|-----------|-------------|
| File name | `Licensees_0.csv` |
| Zipped size | 192 KB |
| Unzipped size | 1.2 MB |
| Variables | 19 |
| Observations |  |

| Variable | Type | Description |
|----------|------|-------------|
| `global_id` | `string` | A unique ID for the licensee. Usually matches other dataset| `s `mme_id` variable. |
| `name` | `string` |  |
| `type` | `string` |  |
| `code` | `string` |  |
| `address1` | `string` |  |
| `address2` | `string` |  |
| `city` | `string` |  |
| `state_code` | `string` |  |
| `postal_code` | `string` |  |
| `country_code` | `string` |  |
| `phone` | `string` |  |
| `external_id` | `string` |  |
| `certificate_number` | `string` |  |
| `is_live` | `bool` |  |
| `suspended` | `bool` |  |
| `created_at` | `datetime` |  |
| `updated_at` | `datetime` |  |
| `deleted_at` | `datetime` |  |
| `expired_at` | `datetime` |  |

## Lab Results Data <a id="lab-results" name="lab-results"></a>

| Data File |  |
|-----------|-------------|
| File name | `LabResults_0.csv`, `LabResults_1.csv`, `LabResults_2.csv` |
| Zipped size | 36 MB, 32 MB, 8 MB |
| Unzipped size | 1.2 GB, 1.1 GB, 135 MB |
| Variables | 71 |
| Observations |  |

| Variable | Type | Description |
|----------|------|-------------|
| `global_id` | `string`  |   |
| `mme_id` | `string` |   |
| `intermediate_type` | `category` |   |
| `status` | `category` |   |
| `global_for_inventory_id` | `string` |   |
| `cannabinoid_status` | `category` |   |
| `cannabinoid_cbc_percent` | `float` |   |
| `cannabinoid_cbc_mg_g` | `float` |   |
| `cannabinoid_cbd_percent` | `float` |   |
| `cannabinoid_cbd_mg_g` | `float` |   |
| `cannabinoid_cbda_percent` | `float` |   |
| `cannabinoid_cbda_mg_g` | `float` |   |
| `cannabinoid_cbdv_percent` | `float` |   |
| `cannabinoid_cbg_percent` | `float` |   |
| `cannabinoid_cbg_mg_g` | `float` |   |
| `cannabinoid_cbga_percent` | `float` |   |
| `cannabinoid_cbga_mg_g` | `float` |   |
| `cannabinoid_cbn_percent` | `float` |   |
| `cannabinoid_cbn_mg_g` | `float` |   |
| `cannabinoid_d8_thc_percent` | `float` |   |
| `cannabinoid_d8_thc_mg_g` | `float` |   |
| `cannabinoid_d9_thca_percent` | `float` |   |
| `cannabinoid_d9_thca_mg_g` | `float` |   |
| `cannabinoid_d9_thc_percent` | `float` |   |
| `cannabinoid_d9_thc_mg_g` | `float` |   |
| `cannabinoid_thcv_percent` | `float` |   |
| `cannabinoid_thcv_mg_g` | `float` |   |
| `solvent_status` | `category` |   |
| `solvent_acetone_ppm` | `float` |   |
| `solvent_benzene_ppm` | `float` |   |
| `solvent_butanes_ppm` | `float` |   |
| `solvent_chloroform_ppm` | `float` |   |
| `solvent_cyclohexane_ppm` | `float` |   |
| `solvent_dichloromethane_ppm` | `float` |   |
| `solvent_ethyl_acetate_ppm` | `float` |   |
| `solvent_heptane_ppm` | `float` |   |
| `solvent_hexanes_ppm` | `float` |   |
| `solvent_isopropanol_ppm` | `float` |   |
| `solvent_methanol_ppm` | `float` |   |
| `solvent_pentanes_ppm` | `float` |   |
| `solvent_propane_ppm` | `float` |   |
| `solvent_toluene_ppm` | `float` |   |
| `solvent_xylene_ppm` | `float` |   |
| `foreign_matter` | `bool` |   |
| `foreign_matter_stems` | `float` |   |
| `foreign_matter_seeds` | `float` |   |
| `microbial_status` | `category` |   |
| `microbial_bile_tolerant_cfu_g` | `float` |   |
| `microbial_pathogenic_e_coli_cfu_g` | `float` |   |
| `microbial_salmonella_cfu_g` | `float` |   |
| `moisture_content_percent` | `float` |   |
| `moisture_content_water_activity_rate` | `float` |   |
| `mycotoxin_status` | `category` |   |
| `mycotoxin_aflatoxins_ppb` | `float` |   |
| `mycotoxin_ochratoxin_ppb` | `float` |   |
| `thc_percent` | `float` |   |
| `notes` | `string` |   |
| `testing_status` | `category` |   |
| `type` | `category` |   |
| `inventory_id` | `string` |   |
| `batch_id` | `string` |   |
| `parent_lab_result_id` | `string` |   |
| `og_parent_lab_result_id` | `string` |   |
| `copied_from_lab_id` | `string` |   |
| `external_id` | `string` |   |
| `lab_user_id` | `string` |   |
| `user_id` | `string` |   |
| `cannabinoid_editor` | `string` |   |
| `microbial_editor` | `string` |   |
| `mycotoxin_editor` | `string` |   |
| `solvent_editor` | `string` |   |

## Inventories and Inventory Type Data <a id="inventory" name="inventory"></a>

*Inventories*

| Data File |  |
|-----------|-------------|
| File name | `Inventories_0.csv` |
| Zipped size | 2.7 GB |
| Unzipped size | 31.7 GB |
| Variables | 27 |
| Observations |  |

| Variable | Type | Description |
|----------|------|-------------|
| `global_id` | `string` |  |
| `strain_id` | `string` |  |
| `inventory_type_id` | `string` |  |
| `qty` | `float` |  |
| `uom` | `string` |  |
| `mme_id` | `string` |  |
| `user_id` | `string` |  |
| `external_id` | `string` |  |
| `area_id` | `string` |  |
| `batch_id` | `string` |  |
| `lab_result_id` | `string` |  |
| `lab_retest_id` | `string` |  |
| `is_initial_inventory` | `bool` |  |
| `created_by_mme_id` | `string` |  |
| `additives` | `string` |  |
| `serving_num` | `float` |  |
| `sent_for_testing` | `bool` |  |
| `medically_compliant` | `string` |  |
| `legacy_id` | `string` |  |
| `lab_results_attested` | `int` |  |
| `global_original_id` | `string` |  |
| `created_at` | `datetime` | No records if issued before 2018-02-21. | 
| `updated_at` | `datetime` |    |
| `deleted_at` | `datetime` |    |
| `inventory_created_at` | `datetime` |  |
| `inventory_packaged_at` | `datetime` |  |
| `lab_results_date` | `datetime` |  |

*Inventory Types*

| Data File |  |
|-----------|-------------|
| File name | `InventoryTypes_0.csv` |
| Zipped size | 1.1 GB |
| Unzipped size | 14.8 GB |
| Variables | 10 |
| Observations | 57,016,229 |

| Variable | Type | Description |
|----------|------|-------------|
| `global_id` | `string` |  |
| `mme_id` | `string` |  |
| `user_id` | `string` |  |
| `external_id` | `string` |  |
| `uom` | `string` |  |
| `name` | `string` |  |
| `intermediate_type` | `string` |  |
| `created_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `deleted_at` | `datetime` |    |


## Strain Data <a id="strains" name="strains"></a>

| Data File |  |
|-----------|-------------|
| File name | `Strains_0.csv` |
| Zipped size | 28 MB |
| Unzipped size | 264 MB |
| Variables | 8 |
| Observations |  |

| Variable | Type | Description |
|----------|------|-------------|
| `mme_id` | `string` |  |
| `user_id` | `string` |  |
| `global_id` | `string` |  |
| `external_id` | `string` |  |
| `name` | `string` |  |
| `created_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `deleted_at` | `datetime` |    |

## Sales and Sale Items Data <a id="sales" name="sales"></a>

*Sales*

| Data File |  |
|-----------|-------------|
| File name | `Sales_0.csv`, `Sales_1.csv`, `Sales_2.csv` |
| Zipped size | 2.8 GB, 4.4 GB, 1.2 GB |
| Unzipped size | 31.1 GB, 37.1 GB, 10.7 GB |
| Variables | 13 |
| Observations |  |

| Variable | Type | Description |
|----------|------|-------------|
| `global_id` | `string` |  |
| `external_id` | `string` |  |
| `type` | `string` | `wholesale` or `retail_recrational` (TODO: confirm this misspelling) |
| `price_total` | `float` |  |
| `status` | `string` |  |
| `mme_id` | `string` |  |
| `user_id` | `string` |  |
| `area_id` | `string` |  |
| `sold_by_user_id` | `string` |  |
| `created_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `sold_at` | `datetime` |  |
| `deleted_at` | `datetime` |    |


*Sale Items*

| Data File |  |
|-----------|-------------|
| File name | `SaleItems_0.csv`, `SaleItems_1.csv`, `SaleItems_2.csv`, `SaleItems_3.csv` |
| Zipped size | 4.7 GB, 5.7 GB, 5.5 GB, 4.6 GB |
| Unzipped size | 42.6 GB, 48.2 GB, 48.5 GB, 41.9 GB |
| Variables | 16 |
| Observations | 346,844,114 |

| Variable | Type | Description |
|----------|------|-------------|
| `global_id` | `string` |  |
| `mme_id` | `string` |  |
| `user_id` | `string` |  |
| `sale_id` | `string` |  |
| `batch_id` | `string` |  |
| `inventory_id` | `string` |  |
| `external_id` | `string` |  |
| `qty` | `float` |  |
| `uom` | `string` |  |
| `unit_price` | `float` |  |
| `price_total` | `float` |  |
| `name` | `string` |  |
| `created_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `sold_at` | `datetime` |  |
| `use_by_date` | `datetime` |  |


## Batches Data <a id="batches" name="batches"></a>

| Data File |  |
|-----------|-------------|
| File name | `Batches_0.csv` |
| Zipped size | 1.3 GB |
| Unzipped size | 27 GB |
| Variables | 44 |
| Observations | 47,292,622 |

| Variable | Type | Description |
|----------|------|-------------|
| `external_id` | `string` |  |
| `num_plants` | `float` |  |
| `status` | `string` |  |
| `qty_harvest` | `float` |  |
| `uom` | `string` |  |
| `is_parent_batch` | `int` |  |
| `is_child_batch` | `int` |  |
| `type` | `string` |  |
| `harvest_stage` | `string` |  |
| `qty_accumulated_waste` | `float` |  |
| `qty_packaged_flower` | `float` |  |
| `qty_packaged_by_product` | `float` |  |
| `origin` | `string` |  |
| `source` | `string` |  |
| `qty_cure` | `float` |  |
| `plant_stage` | `string` |  |
| `flower_dry_weight` | `float` |  |
| `waste` | `float` |  |
| `other_waste` | `float` |  |
| `flower_waste` | `float` |  |
| `other_dry_weight` | `float` |  |
| `flower_wet_weight` | `float` |  |
| `other_wet_weight` | `float` |  |
| `global_id` | `string` |  |
| `global_area_id` | `string` |  |
| `area_name` | `string` |  |
| `global_mme_id` | `string` |  |
| `mme_name` | `string` |  |
| `mme_code` | `string` |  |
| `global_user_id` | `string` |  |
| `global_strain_id` | `string` |  |
| `strain_name` | `string` |  |
| `global_mother_plant_id` | `string` |  |
| `global_flower_area_id` | `string` |  |
| `global_other_area_id` | `string` |  |
| `created_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `planted_at` | `datetime` |  |
| `harvested_at` | `datetime` |  |
| `batch_created_at` | `datetime` |  |
| `deleted_at` | `datetime` |    |
| `est_harvest_at` | `datetime` |  |
| `packaged_completed_at` | `datetime` |  |
| `harvested_end_at` | `datetime` |  |


## Areas Data <a id="areas" name="areas"></a>

| Data File |  |
|-----------|-------------|
| File name | `Areas_0.csv` |
| Zipped size | 9 MB |
| Unzipped size | 81 MB |
| Variables | 8 |
| Observations |  |

| Variable | Type | Description |
|----------|------|-------------|
| `external_id` | `string` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `is_quarantine_area` | `bool` |  |
| `global_id` | `string` |  |
| `created_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `deleted_at` | `datetime` |    |


## Inventory Transfers and Inventory Transfer Items Data <a id="transfers" name="transfers"></a>

*Inventory Transfers*

| Data File |  |
|-----------|-------------|
| File name | `InventoryTransfers_0.csv` |
| Zipped size | 80 MB |
| Unzipped size | 702 MB |
| Variables | 38 |
| Observations |  |

| Variable | Type | Description |
|----------|------|-------------|
| `number_of_edits` | `int` |  |
| `external_id` | `string` |  |
| `void` | `int` |  |
| `multi_stop` | `int` |  |
| `route` | `string` |  |
| `stops` | `string` |  |
| `vehicle_description` | `string` |  |
| `vehicle_year` | `string` |  |
| `vehicle_color` | `string` |  |
| `vehicle_vin` | `string` |  |
| `vehicle_license_plate` | `string` |  |
| `notes` | `string` |  |
| `transfer_manifest` | `string` |  |
| `manifest_type` | `string` |  |
| `status` | `string` |  |
| `type` | `string` |  |
| `transfer_type` | `string` |  |
| `global_id` | `string` |  |
| `test_for_terpenes` | `int` |  |
| `transporter_name1` | `string` |  |
| `transporter_name2` | `string` |  |
| `global_mme_id` | `string` |  |
| `global_user_id` | `string` |  |
| `global_from_mme_id` | `string` |  |
| `global_to_mme_id` | `string` |  |
| `global_from_user_id` | `string` |  |
| `global_to_user_id` | `string` |  |
| `global_from_customer_id` | `string` |  |
| `global_to_customer_id` | `string` |  |
| `global_transporter_user_id` | `string` |  |
| `created_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `hold_starts_at` | `datetime` |    |
| `hold_ends_at` | `datetime` |    |
| `transferred_at` | `datetime` |  |
| `est_departed_at` | `datetime` |  |
| `est_arrival_at` | `datetime` |  |
| `deleted_at` | `datetime` |  |


*Inventory Transfer Items Data*

| Data File |  |
|-----------|-------------|
| File name | `InventoryTransferItems_0.csv` |
| Zipped size | 1 GB |
| Unzipped size | 15.2 GB |
| Variables | 36 |
| Observations |  |

| Variable | Type | Description |
|----------|------|-------------|
| `external_id` | `string` |  |
| `is_sample` | `int` |  |
| `sample_type` | `string` |  |
| `product_sample_type` | `string` |  |
| `description` | `string` |  |
| `qty` | `float` |  |
| `price` | `float` |  |
| `uom` | `string` |  |
| `received_qty` | `float` |  |
| `retest` | `int` |  |
| `global_id` | `string` |  |
| `is_for_extraction` | `int` |  |
| `propagation_source` | `string` |  |
| `inventory_name` | `string` |  |
| `intermediate_type` | `string` |  |
| `strain_name` | `string` |  |
| `global_mme_id` | `string` |  |
| `global_user_id` | `string` |  |
| `global_batch_id` | `string` |  |
| `global_plant_id` | `string` |  |
| `global_inventory_id` | `string` |  |
| `global_lab_result_id` | `string` |  |
| `global_received_area_id` | `string` |  |
| `global_received_strain_id` | `string` |  |
| `global_inventory_transfer_id` | `string` |  |
| `global_received_batch_id` | `string` |  |
| `global_received_inventory_id` | `string` |  |
| `global_received_plant_id` | `string` |  |
| `global_received_mme_id` | `string` |  |
| `global_received_mme_user_id` | `string` |  |
| `global_customer_id` | `string` |  |
| `global_inventory_type_id` | `string` |  |
| `created_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `received_at` | `datetime` |    |
| `deleted_at` | `datetime` |    |


## Disposals Data <a id="disposals" name="disposals"></a>

| Data File |  |
|-----------|-------------|
| File name | `Disposals_0.csv` |
| Zipped size | 788 MB |
| Unzipped size | 10 GB |
| Variables | 23 |
| Observations |  |

| Variable | Type | Description |
|----------|------|-------------|
| `external_id` | `string` |  |
| `whole_plant` | `string` |  |
| `reason` | `string` |  |
| `method` | `string` |  |
| `phase` | `string` |  |
| `type` | `string` |  |
| `qty` | `float` |  |
| `uom` | `string` |  |
| `source` | `string` |  |
| `disposal_cert` | `string` |  |
| `global_id` | `string` |  |
| `global_mme_id` | `string` |  |
| `global_user_id` | `string` |  |
| `global_batch_id` | `string` |  |
| `global_area_id` | `string` |  |
| `global_plant_id` | `string` |  |
| `global_inventory_id` | `string` |  |
| `created_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `hold_starts_at` | `datetime` |    |
| `hold_ends_at` | `datetime` |    |
| `disposal_at` | `datetime` |    |
| `deleted_at` | `datetime` |    |


## Inventory Adjustments Data <a id="adjustments" name="adjustments"></a>

| Data Files |  |
|-----------|-------------|
| File name | `InventoryAdjustments_0.csv`, `InventoryAdjustments_1.csv`, `InventoryAdjustments_2.csv` |
| Zipped size | 1.5 GB, 1.5 GB, 1.4 GB |
| Unzipped size |  |
| Variables | 14 |
| Observations |  |

| Variable | Type | Description |
|----------|------|-------------|
| `external_id` | `string` |  |
| `qty` | `float` |  |
| `uom` | `string` |  |
| `reason` | `string` |  |
| `memo` | `string` |  |
| `global_id` | `string` |  |
| `global_mme_id` | `string` |  |
| `global_user_id` | `string` |  |
| `global_inventory_id` | `string` |  |
| `global_adjusted_by_user_id` | `string` |  |
| `created_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `adjusted_at` | `datetime` |    |
| `deleted_at` | `datetime` |    |


## Plants Data <a id="plants" name="plants"></a>

| Data File |  |
|-----------|-------------|
| File name | `Plants_0.csv` |
| Zipped size | 379 MB |
| Unzipped size | 12.9 GB |
| Variables | 21 |
| Observations | 30,538,973 |

| Variable | Type | Description |
|----------|------|-------------|
| `global_id` | `string` |  |
| `mme_id` | `string` |  |
| `user_id` | `string` |  |
| `external_id` | `string` |  |
| `inventory_id` | `string` |  |
| `batch_id` | `string` |  |
| `area_id` | `string` |  |
| `mother_plant_id` | `string` |  |
| `is_initial_inventory` | `string` |  |
| `origin` | `string` |  |
| `stage` | `string` |  |
| `strain_id` | `string` |  |
| `is_mother` | `string` |  |
| `last_moved_at` | `string` |  |
| `legacy_id` | `string` |  |
| `created_at` | `datetime` |    |
| `deleted_at` | `datetime` |    |
| `updated_at` | `datetime` |    |
| `plant_created_at` | `datetime` |    |
| `plant_harvested_at` | `datetime` |    |
| `plant_harvested_end_at` | `datetime` |    |


## Data Sources

- WA State Traceability Data January 2018 - November 2021
  * <https://lcb.app.box.com/s/e89t59s0yb558tjoncjsid710oirqbgd?page=1>
  * <https://lcb.app.box.com/s/e89t59s0yb558tjoncjsid710oirqbgd?page=2>
