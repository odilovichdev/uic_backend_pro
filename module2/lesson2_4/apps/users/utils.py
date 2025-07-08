import string
import random
import requests


def generate_code(code_length=6):
    return ''.join(random.choices(string.digits, k=code_length))


def generate_session(session_length=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=session_length))


def generate_cache_key(*args):
    return "phone_sms_" + "_".join(arg for arg in args)


def send_single_sms(phone_number: str, code: str):
    """Generate SMS text and save it to the model"""

    headers = {
        "Authorization": 'Token 3d2b422e9b1d4241be0fc9fd1cd6c7e6790c9822',
        'Content-Type': 'application/json'
    }

    json_data = {
        "phone_number": phone_number,
        'template_id': 112,
        'template_params': {
            'code': code
        }
    }

    # send sms
    try:
        response = requests.post('https://semes.xn--h28h.uz/api/v1/sms/send',
                                 headers=headers,
                                 json=json_data,
                                 timeout=5)

        if response.text == 'Request is received':
            return True

        if not response.ok:
            return False

    except requests.RequestException as e:
        print(f"Error sending sms: {e}")
        return False