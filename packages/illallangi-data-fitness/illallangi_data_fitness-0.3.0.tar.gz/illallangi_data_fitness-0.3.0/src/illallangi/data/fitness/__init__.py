import djp
from django.urls import URLPattern, re_path

from illallangi.data.fitness import checks  # noqa: F401


@djp.hookimpl
def installed_apps() -> list[str]:
    return [
        "illallangi.data.fitness",
    ]


@djp.hookimpl
def urlpatterns() -> list[URLPattern]:
    from illallangi.data.fitness import views

    return [
        re_path(
            r"^swims/$",
            views.swims_html,
            name="swims_html",
        ),
        re_path(
            r"^swims/(?P<swim_year>[0-9]{4})/$",
            views.swims_html,
            name="swims_year",
        ),
        re_path(
            r"^swims/(?P<swim_year>[0-9]{4})/(?P<swim_month>[0-9]{2})/$",
            views.swims_html,
            name="swims_month",
        ),
        re_path(
            r"^swims/(?P<swim_year>[0-9]{4})/(?P<swim_month>[0-9]{2})/(?P<swim_day>[0-9]{2})/$",
            views.swims_html,
            name="swims_day",
        ),
        re_path(
            r"^swims/(?P<swim_year>[0-9]{4})/(?P<swim_month>[0-9]{2})/(?P<swim_day>[0-9]{2})/(?P<swim_slug>[\w\d-]+)/$",
            views.swim_html,
            name="swim_html",
        ),
    ]
