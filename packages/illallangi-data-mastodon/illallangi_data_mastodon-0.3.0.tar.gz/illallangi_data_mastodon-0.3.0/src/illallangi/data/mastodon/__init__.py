import djp
from django.urls import URLPattern, re_path

from illallangi.data.mastodon import checks  # noqa: F401


@djp.hookimpl
def installed_apps() -> list[str]:
    return [
        "illallangi.data.mastodon",
    ]


@djp.hookimpl
def urlpatterns() -> list[URLPattern]:
    from illallangi.data.mastodon import views

    return [
        re_path(
            r"^statuses/$",
            views.statuses_html,
            name="statuses_html",
        ),
        re_path(
            r"^statuses/(?P<status_year>[0-9]{4})/$",
            views.statuses_html,
            name="statuses_year",
        ),
        re_path(
            r"^statuses/(?P<status_year>[0-9]{4})/(?P<status_month>[0-9]{2})/$",
            views.statuses_html,
            name="statuses_month",
        ),
        re_path(
            r"^statuses/(?P<status_year>[0-9]{4})/(?P<status_month>[0-9]{2})/(?P<status_day>[0-9]{2})/$",
            views.statuses_html,
            name="statuses_day",
        ),
        re_path(
            r"^statuses/(?P<status_year>[0-9]{4})/(?P<status_month>[0-9]{2})/(?P<status_day>[0-9]{2})/(?P<status_slug>[\w\d-]+)/$",
            views.status_html,
            name="status_html",
        ),
    ]
