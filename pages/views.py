from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import LeadForm
from urllib.parse import urlencode, urlsplit, urlunsplit, parse_qsl


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
    return render(request, "pages/telegram.html")


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
        # TODO: send to CRM / Telegram / email, save to DB, etc.
        # For now we just redirect back (next/referer) and show success modal.
        next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or ""
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
            parts = urlsplit(next_url)
            q = dict(parse_qsl(parts.query, keep_blank_values=True))
            q["lead_success"] = "1"
            new_url = urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(q), parts.fragment))
            return redirect(new_url)
        return redirect(reverse("home_page") + "?lead_success=1")

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
