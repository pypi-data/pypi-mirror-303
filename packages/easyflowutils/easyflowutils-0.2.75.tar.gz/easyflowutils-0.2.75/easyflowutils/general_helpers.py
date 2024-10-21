import urllib.parse


def get_whatsapp_url(phone_number: str, text: str) -> str:
    encoded_text = urllib.parse.quote(text)
    return f"https://wa.me/972{phone_number}?text={encoded_text}"
