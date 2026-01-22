from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home_page"),
    path("home/lead/", views.submit_lead, name="submit_lead"),
    path("cookie-policy/", views.cookie_policy, name="cookie_policy"),
    path("billboards/", views.billboards, name="billboards"),
    path("transport/", views.transport, name="transport"),
    path("stops/", views.stops, name="stops"),
    path("radio/", views.radio, name="radio"),
    path("elevators/", views.elevators, name="elevators"),
    path("ai-assistants/", views.ai_assistants, name="ai_assistants"),
    path("telegram/", views.telegram, name="telegram"),
    path("design/", views.design, name="design"),
    path("print/", views.print_polygraphy, name="print_polygraphy"),
    path("production/", views.production, name="production"),
    path("404/", views.preview_404, name="preview_404"),
    path("styleguide/", views.styleguide, name="styleguide"),
    path("health/", views.health, name="health"),
]


