from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.education.models import Course


@require_GET
def course_html(
    request: HttpRequest,
    course_slug: str,
    **_: dict,
) -> render:
    objects = Course.objects.filter(slug=course_slug)

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple courses found for slug",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "education/course.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Courses",
                        "url": reverse(
                            "courses_html",
                        ),
                    },
                    {
                        "title": str(obj),
                        "url": obj.get_absolute_url(),
                    },
                ],
                "links": [
                    {
                        "rel": "alternate",
                        "type": "text/html",
                        "href": request.build_absolute_uri(
                            obj.get_absolute_url(),
                        ),
                    },
                ],
            },
        )

    return HttpResponse(
        status=400,
        content="Course not found",
    )
