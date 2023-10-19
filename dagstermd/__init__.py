import os
from dagster import Definitions, file_relative_path
from dagster_dbt import DbtCliResource
from dagster_duckdb_pandas import DuckDBPandasIOManager
from .resources import YnabClientResource

from .assets import ynab_assets, depot_dbt_assets

DBT_PROJECT_DIR = file_relative_path(__file__, "./depot")
DBT_PROFILES_DIR = file_relative_path(__file__, "./depot")

all_assets = [
    *ynab_assets,
    depot_dbt_assets,
]

defs = Definitions(
    assets=all_assets,
    resources={
        'ynab_api': YnabClientResource(
            personal_token = os.environ['YNAB_PERSONAL_TOKEN'],
            budget_id = os.environ['YNAB_BUDGET_ID'],
        ),
        'source_io_manager': DuckDBPandasIOManager(database=f'md:depot', schema="source"),
        'dbt': DbtCliResource(project_dir=DBT_PROJECT_DIR, profiles_dir=DBT_PROFILES_DIR),
    }
)
