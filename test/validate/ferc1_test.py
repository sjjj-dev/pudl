"""
Validate post-ETL FERC Form 1 data and the associated derived outputs.

These tests depend on a FERC Form 1 specific PudlTabl output object, which is
a parameterized fixture that has session scope.
"""
import logging

import pandas as pd
import pytest

from pudl import validate as pv
from pudl.settings import Ferc1Settings

logger = logging.getLogger(__name__)

# These are tables for which individual records have been sliced up and
# turned into columns -- so there's no universally unique record ID:
row_mapped_tables = [
    "plant_in_service_ferc1",
]
unique_record_tables = [
    t for t in Ferc1Settings.tables if t not in row_mapped_tables
]


@pytest.mark.parametrize("table_name", unique_record_tables)
def test_record_id_dupes(pudl_engine, table_name):
    """Verify that the generated ferc1 record_ids are unique."""
    table = pd.read_sql(table_name, pudl_engine)
    n_dupes = table.record_id.duplicated().values.sum()

    if n_dupes:
        dupe_ids = (table.record_id[table.record_id.duplicated()].values)
        raise AssertionError(
            f"{n_dupes} duplicate record_ids found in "
            f"{table_name}: {dupe_ids}."
        )


@pytest.mark.parametrize(
    "df_name,cols", [
        ("all_plants_ferc1", "all"),
        ("fbp_ferc1", "all"),
        ("fuel_ferc1", "all"),
        ("plant_in_service_ferc1", "all"),
        ("plants_hydro_ferc1", "all",),
        ("plants_pumped_storage_ferc1", "all"),
        ("plants_small_ferc1", "all"),
        ("plants_steam_ferc1", "all"),
        ("pu_ferc1", "all"),
        ("purchased_power_ferc1", "all"),
    ])
def test_no_null_cols_ferc1(pudl_out_ferc1, live_dbs, cols, df_name):
    """Verify that output DataFrames have no entirely NULL columns."""
    if not live_dbs:
        pytest.skip("Data validation only works with a live PUDL DB.")
    pv.no_null_cols(
        pudl_out_ferc1.__getattribute__(df_name)(),
        cols=cols, df_name=df_name)


@pytest.mark.parametrize(
    "df_name,expected_rows", [
        ('all_plants_ferc1', 51_456),
        ('fbp_ferc1', 20_573),
        ('fuel_ferc1', 31_265),
        ('plant_in_service_ferc1', 26_933),
        ('plants_hydro_ferc1', 6_782),
        ('plants_pumped_storage_ferc1', 710),
        ('plants_small_ferc1', 15_584),
        ('plants_steam_ferc1', 28_380),
        ('pu_ferc1', 6_946),
        ('purchased_power_ferc1', 190_228)
    ]
)
def test_minmax_rows(pudl_out_ferc1, live_dbs, expected_rows, df_name):
    """Verify that output DataFrames don't have too many or too few rows.

    Args:
        pudl_out_ferc1: A PudlTabl output object.
        live_dbs: Boolean (wether we're using a live or testing DB).
        expected_rows (int): Expected number of rows that the dataframe should
            contain when all data is loaded and is output without aggregation.
        df_name (str): Shorthand name identifying the dataframe, corresponding
            to the name of the function used to pull it from the PudlTabl
            output object.

    """
    if not live_dbs:
        pytest.skip("Data validation only works with a live PUDL DB.")
    _ = (
        pudl_out_ferc1.__getattribute__(df_name)()
        .pipe(pv.check_min_rows, expected_rows=expected_rows,
              margin=0.0, df_name=df_name)
        .pipe(pv.check_max_rows, expected_rows=expected_rows,
              margin=0.0, df_name=df_name)
    )


@pytest.mark.parametrize(
    "df_name,unique_subset", [
        ("pu_ferc1", ["utility_id_ferc1", "plant_name_ferc1"]),
        ("fbp_ferc1", [
            "report_year",
            "utility_id_ferc1",
            "plant_name_ferc1"
        ]),
        ("plants_hydro_ferc1", [
            "report_year",
            "utility_id_ferc1",
            "plant_name_ferc1",
            "capacity_mw"  # Why does having capacity here make sense???
        ]),
        ("plants_pumped_storage_ferc1", [
            "report_year",
            "utility_id_ferc1",
            "plant_name_ferc1",
            "capacity_mw"  # Why does having capacity here make sense???
        ]),
        ("plant_in_service_ferc1", [
            "report_year",
            "utility_id_ferc1",
            "amount_type"
        ]),
    ]
)
def test_unique_rows_ferc1(pudl_out_ferc1, live_dbs, df_name, unique_subset):
    """Test whether dataframe has unique records within a subset of columns."""
    if not live_dbs:
        pytest.skip("Data validation only works with a live PUDL DB.")
    pv.check_unique_rows(
        pudl_out_ferc1.__getattribute__(df_name)(),
        subset=unique_subset, df_name=df_name)
