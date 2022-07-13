from app.utils.phyllo_api import get_all_income, get_income_by_id


def get_all(query_param: dict):
    incomes = get_all_income(query_param=query_param)
    # Add business logic here
    return incomes


def get_by_id(id: str, query_param: dict):
    income = get_income_by_id(id=id)
    # Add business logic here
    return income
