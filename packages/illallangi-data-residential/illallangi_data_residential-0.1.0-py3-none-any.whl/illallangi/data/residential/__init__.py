import djp
from django.urls import URLPattern, re_path

from illallangi.data.residential import checks  # noqa: F401


@djp.hookimpl
def installed_apps() -> list[str]:
    return [
        "illallangi.data.residential",
    ]


@djp.hookimpl
def urlpatterns() -> list[URLPattern]:
    from illallangi.data.residential import views

    return [
        re_path(
            r"^residences/$",
            views.residences_html,
            name="residences_html",
        ),
        re_path(
            r"^residences/(?P<residence_slug>[\w\d-]+)/$",
            views.residence_html,
            name="residence_html",
        ),
    ]
