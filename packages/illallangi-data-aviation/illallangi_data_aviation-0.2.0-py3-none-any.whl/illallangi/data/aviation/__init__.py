import djp
from django.urls import URLPattern, re_path

from illallangi.data.aviation import checks  # noqa: F401


@djp.hookimpl
def installed_apps() -> list[str]:
    return [
        "illallangi.data.aviation",
        "colorfield",
    ]


@djp.hookimpl
def urlpatterns() -> list[URLPattern]:
    from illallangi.data.aviation import views

    return [
        re_path(
            r"^airlines/$",
            views.airlines_html,
            name="airlines_html",
        ),
        re_path(
            r"^airlines/(?P<airline_slug>[\w\d-]+)/$",
            views.airline_html,
            name="airline_html",
        ),
        re_path(
            r"^airports/$",
            views.airports_html,
            name="airports_html",
        ),
        re_path(
            r"^airports/(?P<airport_slug>[\w\d-]+)/$",
            views.airport_html,
            name="airport_html",
        ),
        re_path(
            r"^alliances/$",
            views.alliances_html,
            name="alliances_html",
        ),
        re_path(
            r"^alliances/(?P<alliance_slug>[\w\d-]+)/$",
            views.alliance_html,
            name="alliance_html",
        ),
    ]
