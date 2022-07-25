from decouple import config, Csv

CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")
BASE_URL = config("BASE_URL")
WEBHOOK_URL = config("WEBHOOK_URL")
SUPPORTED_WEBHOOK_EVENTS = config('SUPPORTED_WEBHOOK_EVENTS', cast=Csv())
