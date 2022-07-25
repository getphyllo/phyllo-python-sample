from app.utils.phyllo_api import get_all_work_platfrom, get_work_platform_by_id


def get_all(query_param: dict):
    work_platforms = get_all_work_platfrom(query_param=query_param)
    # Add business logic here
    return work_platforms


def get_by_id(id: str):
    work_platform = get_work_platform_by_id(id=id)
    # Add business logic here
    return work_platform
