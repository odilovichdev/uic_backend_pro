import time

from core.celery import app


@app.task
def send_single_sms_task(phone_number: str, code: str) -> bool:
    """User ga sms yuboradigan celery task"""
    from apps.users.utils import send_single_sms
    time.sleep(15)
    print(f"Time sleep 5 -----")
    return send_single_sms(phone_number, code)