import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.fitness.models import Swim


@require_GET
def swim_html(
    request: HttpRequest,
    swim_slug: str,
    **_: dict,
) -> render:
    objects = Swim.objects.filter(sqid=swim_slug)

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple swims found for slug",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "fitness/swim.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Swims",
                        "url": reverse(
                            "swims_html",
                        ),
                    },
                    {
                        "title": obj.date.year,
                        "url": reverse(
                            "swims_year",
                            kwargs={
                                "swim_year": str(obj.date.year).zfill(4),
                            },
                        ),
                    },
                    {
                        "title": calendar.month_name[obj.date.month],
                        "url": reverse(
                            "swims_month",
                            kwargs={
                                "swim_year": str(obj.date.year).zfill(4),
                                "swim_month": str(obj.date.month).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": ordinal(obj.date.day),
                        "url": reverse(
                            "swims_day",
                            kwargs={
                                "swim_year": str(obj.date.year).zfill(4),
                                "swim_month": str(obj.date.month).zfill(2),
                                "swim_day": str(obj.date.day).zfill(2),
                            },
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
        content="Swim not found",
    )
