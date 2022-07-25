from app.utils.phyllo_api import get_audience


def get(query_param: dict):
    audience_data = get_audience(query_param=query_param)
    # Add business logic here
    return audience_data
