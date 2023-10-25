import pandas as pd
from dagster import asset
from dagstermd.resources import YnabClientResource

@asset(compute_kind='duckdb', io_manager_key='source_io_manager')
def ynab_accounts(ynab_api: YnabClientResource) -> pd.DataFrame:
    accounts_result = ynab_api.get_accounts_data()
    accounts_df = pd.DataFrame([
        {
            'id': n.get('id'),
            'name': n.get('name'),
            'type': n.get('type'),
            'on_budget': n.get('on_budget'),
            'closed': n.get('closed'),
            'balance': n.get('balance'),
            'cleared_balance': n.get('cleared_balance'),
            'uncleared_balance': n.get('uncleared_balance'),
            'deleted': n.get('deleted'),
            'data_insertion_timestamp': pd.Timestamp.now()  
        }
        for n in accounts_result.get('data').get('accounts')
    ])
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

@asset(compute_kind='duckdb', io_manager_key='source_io_manager')
def ynab_transactions(ynab_api: YnabClientResource) -> pd.DataFrame:
    transactions_result = ynab_api.get_transactions_data()
    transactions_df = pd.DataFrame(transactions_result.get('data').get('transactions'))
    return transactions_df

@asset(compute_kind='duckdb', io_manager_key='source_io_manager')
def ynab_payees(ynab_api: YnabClientResource) -> pd.DataFrame:
    budget_result = ynab_api.get_budgets_data()
    payees = budget_result.get('data').get('budget').get('payees')
    payees_df = pd.DataFrame(payees)
    return payees_df
