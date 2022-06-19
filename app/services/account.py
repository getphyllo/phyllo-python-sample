from app.utils.phyllo_api import get_all_account, get_account_by_id


def get_all(query_param: dict):
    accounts = get_all_account(query_param)
    # Add buissness logic here
    return accounts



def get_by_id(id: str):
    account = get_account_by_id(id=id)
    # Add buissness logic here
    return account
