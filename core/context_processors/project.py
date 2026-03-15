import os
from datetime import datetime
from urllib.parse import quote

from django.conf import settings


def project(request):
    """
    Small set of globals available in all templates.
    Keep it minimal and stable for design/pixel-perfect work.
    """
    base_url = (request.build_absolute_uri("/").rstrip("/") if request else "") or ""
    telegram_cases_url = getattr(settings, "TELEGRAM_CASES_URL", "") or ""
    default_cases_url = getattr(settings, "CASES_URL", "") or ""
    if not default_cases_url and base_url:
        default_cases_url = f"{base_url}#cases"
    elif default_cases_url and base_url and not default_cases_url.startswith(("http://", "https://")):
        default_cases_url = (base_url.rstrip("/") + default_cases_url) if default_cases_url.startswith("#") else (base_url.rstrip("/") + "/" + default_cases_url.lstrip("/"))
    url_name = getattr(getattr(request, "resolver_match", None), "url_name", None) if request else None
    cases_url = telegram_cases_url if url_name == "telegram" else (default_cases_url or "#")
    contact_phone = getattr(settings, "CONTACT_PHONE", "") or "79179816000"
    contact_phone_digits = "".join(c for c in contact_phone if c.isdigit())
    contact_email = (getattr(settings, "CONTACT_EMAIL", "") or "").strip() or "welcome@ad-smart.ru"
    tg_channel = getattr(settings, "CONTACT_TELEGRAM_CHANNEL", "") or "artm_medvedev"
    tg_channel = tg_channel.strip().lstrip("@")
    # Ссылка «написать на почту» — открывает Gmail в новой вкладке (без диалога «Открыть с помощью»)
    footer_email_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={quote(contact_email)}" if contact_email else "#"
    return {
        "PROJECT_NAME": os.getenv("PROJECT_NAME", "ADSmart"),
        "CURRENT_YEAR": datetime.now().year,
        "FOOTER_PHONE_URL": f"tel:+{contact_phone_digits}" if contact_phone_digits else "#",
        "FOOTER_TELEGRAM_URL": f"https://t.me/{tg_channel}" if tg_channel else "#",
        "FOOTER_EMAIL": contact_email,
        "FOOTER_EMAIL_URL": footer_email_url,
        "CONTACT_PHONE": contact_phone_digits,
        "CONTACT_PHONE_DISPLAY": getattr(settings, "CONTACT_PHONE_DISPLAY", "") or "+7 (917) 981-60-00",
        "CONTACT_EMAIL": contact_email,
        "CASES_URL": cases_url or "#",
        "TELEGRAM_CASES_URL": telegram_cases_url or "#",
        "DEFAULT_CASES_URL": default_cases_url or "#",
    }



