from app.utils.phyllo_api import get_all_profile,get_profile_by_id


def get_all(query_param: dict):
    profiles = get_all_profile(query_param=query_param)
    # Add business logic here
    return profiles

def get_by_id(id: str):
    profile = get_profile_by_id(id=id)
    # Add business logic here
    return profile