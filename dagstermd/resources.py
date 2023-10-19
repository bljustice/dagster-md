from dagster import ConfigurableResource
from typing import Any

from ynab.accounts import Accounts
from ynab.budgets import Budgets
from ynab.categories import Categories
from ynab.transactions import Transactions

class YnabClientResource(ConfigurableResource):
    personal_token: str
    budget_id: str

    def get_accounts_data(self) -> dict[str, Any]:
        client = Accounts(self.personal_token)
        return client.get_accounts_by_budget_id(self.budget_id)
    
    def get_budgets_data(self) -> dict[str, Any]:
        client = Budgets(self.personal_token)
        return client.get_budget_by_id(self.budget_id)
    
    def get_categories_data(self) -> dict[str, Any]:
        client = Categories(self.personal_token)
        return client.get_categories_by_budget_id(self.budget_id)
    
    def get_transactions_data(self) -> dict[str, Any]:
        client = Transactions(self.personal_token)
        return client.get_transactions_by_budget_id(self.budget_id)
