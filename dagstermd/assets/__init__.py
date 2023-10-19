from . import ynab
from dagster import load_assets_from_package_module, file_relative_path, AssetExecutionContext
from dagster_dbt import dbt_assets, DbtCliResource

DBT_MANIFEST = file_relative_path(__file__, '../depot/target/manifest.json')
DBT_PROJECT_DIR = file_relative_path(__file__, "../depot")
DBT_PROFILES_DIR = file_relative_path(__file__, "../depot")

@dbt_assets(manifest=DBT_MANIFEST)
def depot_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

ynab_assets = load_assets_from_package_module(package_module=ynab, group_name="ynab")
