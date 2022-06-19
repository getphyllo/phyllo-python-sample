from app.utils.phyllo_api import create_sdk_token


def create(body: dict):
    sdk_token = create_sdk_token(body=body)
    # Add business logic here
    return sdk_token