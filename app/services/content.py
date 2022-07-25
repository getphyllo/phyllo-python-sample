from app.utils.phyllo_api import get_all_content, get_content_by_id


def get_all(query_param: dict):
    contents = get_all_content(query_param=query_param)
    # Add business logic here
    return contents


def get_by_id(id: str):
    content = get_content_by_id(id=id)
    # Add business logic here
    return content
