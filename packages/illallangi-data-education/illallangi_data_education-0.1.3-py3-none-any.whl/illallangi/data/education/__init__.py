import djp
from django.urls import URLPattern, re_path

from illallangi.data.education import checks  # noqa: F401


@djp.hookimpl
def installed_apps() -> list[str]:
    return [
        "illallangi.data.education",
    ]


@djp.hookimpl
def urlpatterns() -> list[URLPattern]:
    from illallangi.data.education import views

    return [
        re_path(
            r"^courses/$",
            views.courses_html,
            name="courses_html",
        ),
        re_path(
            r"^courses/(?P<course_slug>[\w\d-]+)/$",
            views.course_html,
            name="course_html",
        ),
    ]
