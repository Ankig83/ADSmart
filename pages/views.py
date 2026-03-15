import logging
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit, urlparse

# import requests  # было для Telegram
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import LeadForm

logger = logging.getLogger(__name__)


def home(request):
    return render(request, "pages/home.html")


def styleguide(request):
    return render(request, "pages/styleguide.html")

def cookie_policy(request):
    return render(request, "pages/cookie_policy.html")

def billboards(request):
    return render(request, "pages/billboards.html")

def transport(request):
    return render(request, "pages/transport.html")


def stops(request):
    return render(request, "pages/stops.html")

def radio(request):
    return render(request, "pages/radio.html")

def elevators(request):
    return render(request, "pages/elevators.html")


def ai_assistants(request):
    return render(request, "pages/ai_assistants.html")


def telegram(request):
    tg_platform_cells = [
        "Риск наткнуться на каналы с ботами или низкой вовлеченностью",
        "Риск штрафов из-за ошибок в маркировке рекламы",
        "Высокий риск бана за нарушение правил коммуникации (спам)",
        "Telegram существует в отрыве от общей стратегии",
    ]
    tg_partner_cells = [
        "Глубокий анализ каналов (ER, охваты, цитируемость) — только проверенные площадки",
        "Полная ответственность за корректную маркировку рекламы",
        "Проактивное ведение и модерация — диалог вместо рассылок, защита репутации",
        "Интеграция в гибридную экосистему: QR с билбордов и боты из радио ведут в Telegram",
    ]
    return render(
        request,
        "pages/telegram.html",
        {"tg_platform_cells": tg_platform_cells, "tg_partner_cells": tg_partner_cells},
    )


def design(request):
    return render(request, "pages/design.html")


def print_polygraphy(request):
    return render(request, "pages/print.html")


def production(request):
    return render(request, "pages/production.html")


def health(request):
    return HttpResponse("OK", content_type="text/plain; charset=utf-8")


@require_POST
def submit_lead(request):
    form = LeadForm(request.POST)
    if form.is_valid():
        cleaned = form.cleaned_data
        name = (cleaned.get("name") or cleaned.get("company") or "").strip() or "-"
        phone = (cleaned.get("phone") or "").strip() or "-"
        business = (cleaned.get("business") or cleaned.get("company") or "").strip() or "-"
        source = (cleaned.get("source") or "").strip() or "-"
        form_type = (cleaned.get("type") or "").strip() or "-"
        interest = (cleaned.get("interest_format") or "").strip() or "-"
        page_raw = request.POST.get("page") or request.POST.get("next")
        if page_raw:
            page = page_raw.split("?")[0].split("#")[0].strip()
        else:
            ref = request.META.get("HTTP_REFERER") or ""
            page = urlparse(ref).path if ref.startswith("http") else (ref.split("?")[0].split("#")[0].strip() if ref else request.get_full_path().split("?")[0])

        message_lines = [
            "🚀 Новая заявка",
            "",
            f"Имя: {name}",
            f"Телефон: {phone}",
            f"Сфера бизнеса: {business}",
            f"Страница: {page}",
            f"Блок: {source}",
            f"Тип формы: {form_type}",
        ]
        if interest and interest != "-":
            message_lines.append(f"Доп: {interest}")
        text = "\n".join(message_lines)

        # Email-рассылка всем админам из ADMIN_EMAILS
        admin_emails = getattr(settings, "ADMIN_EMAILS", None)
        if admin_emails:
            recipient_list = [email for _, email in admin_emails]
            try:
                send_mail(
                    subject="🚀 Новая заявка с сайта ADSmart",
                    message=text,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
                logger.info("Lead sent via email: phone=%s, source=%s, recipients=%s", phone, source, recipient_list)
            except Exception as exc:
                logger.exception("Error sending lead email: %s", exc)

        # --- Telegram отправка отключена, переход на email-рассылку ---
        # bot_token = getattr(settings, "TELEGRAM_BOT_TOKEN", None)
        # chat_id = getattr(settings, "TELEGRAM_CHAT_ID", None)
        # if bot_token and chat_id:
        #     url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        #     payload = {"chat_id": str(chat_id), "text": text}
        #     try:
        #         resp = requests.post(url, data=payload, timeout=5)
        #         if resp.ok:
        #             logger.info("Lead sent to Telegram: phone=%s, source=%s", phone, source)
        #         else:
        #             logger.error(
        #                 "Telegram API HTTP error: status=%s body=%s",
        #                 resp.status_code,
        #                 resp.text[:500],
        #             )
        #     except requests.RequestException as exc:
        #         logger.exception("Error sending lead to Telegram: %s", exc)
        # else:
        #     logger.warning(
        #         "Telegram not configured (TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID missing). Lead phone=%s",
        #         phone,
        #     )

        next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or ""
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
            parts = urlsplit(next_url)
            q = dict(parse_qsl(parts.query, keep_blank_values=True))
            q["lead_success"] = "1"
            new_url = urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(q), parts.fragment))
            return redirect(new_url)
        return redirect(reverse("home_page") + "?lead_success=1")

    logger.debug("Lead form invalid: errors=%s", form.errors)
    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or ""
    if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
        parts = urlsplit(next_url)
        q = dict(parse_qsl(parts.query, keep_blank_values=True))
        q["lead_error"] = "1"
        new_url = urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(q), parts.fragment))
        return redirect(new_url)
    return redirect(reverse("home_page") + "?lead_error=1")


def preview_404(request):
    # Preview route for development (DEBUG=True) to see the custom 404 template.
    return render(request, "404.html", status=404)
