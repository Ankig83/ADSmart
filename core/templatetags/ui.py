from django import template
from django.urls import resolve

register = template.Library()


@register.simple_tag(takes_context=True)
def active_class(context, url_name: str, css_class: str = "is-active") -> str:
    """
    Usage:
      <a class="..." href="{% url 'home' %}">{% active_class 'home' %}</a>
    """
    request = context.get("request")
    if request is None:
        return ""
    try:
        match = resolve(request.path_info)
    except Exception:
        return ""
    return css_class if match.url_name == url_name else ""



