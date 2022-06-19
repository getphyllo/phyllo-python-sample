from app.utils.phyllo_api import get_all_user, get_user_by_id, create_user


def create(body: dict):
    user = create_user(body=body)
    # Add business logic here
    return user

def get_all(query_param: dict):
    users = get_all_user(query_param=query_param)
    # Add business logic here
    return users

def get_by_id(id: str):
    user = get_user_by_id(id=id)
    # Add business logic here
    return user