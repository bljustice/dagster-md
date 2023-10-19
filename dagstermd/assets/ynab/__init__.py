import pandas as pd
from dagster import asset
from dagstermd.resources import YnabClientResource

@asset(compute_kind='duckdb', io_manager_key='source_io_manager')
def ynab_accounts(ynab_api: YnabClientResource) -> pd.DataFrame:
    accounts_result = ynab_api.get_accounts_data()
    needed_fields = accounts_result.get('data').get('accounts')[0]
    accounts_df = pd.DataFrame([{
        'id': needed_fields.get('id'),
        'name': needed_fields.get('name'),
        'type': needed_fields.get('type'),
        'on_budget': needed_fields.get('on_budget'),
        'closed': needed_fields.get('closed'),
        'balance': needed_fields.get('balance'),
        'cleared_balance': needed_fields.get('cleared_balance'),
        'uncleared_balance': needed_fields.get('uncleared_balance'),
        'deleted': needed_fields.get('deleted'),
        'data_insertion_timestamp': pd.Timestamp.now()  
    }])
    return accounts_df

@asset(compute_kind='duckdb', io_manager_key='source_io_manager')
def ynab_categories(ynab_api: YnabClientResource) -> pd.DataFrame:
    categories_result = ynab_api.get_categories_data()
    needed_fields = [
        c for x in categories_result.get('data').get('category_groups')
        for c in x.get('categories')
    ]
    categories_df = pd.DataFrame(needed_fields)
    return categories_df
