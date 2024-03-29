from app.webhook.webhook_service import get_all_webhooks, create_webhook, update_webhook


def configure_webhook():
    webhooks = dict(get_all_webhooks())
    if len(webhooks["data"]) == 0:
        create_webhook()
    else:
        webhook_id = webhooks["data"][0]["id"]
        update_webhook(id=webhook_id)
