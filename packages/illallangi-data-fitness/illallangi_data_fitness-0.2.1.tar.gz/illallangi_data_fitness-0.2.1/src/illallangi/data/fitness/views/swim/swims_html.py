import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.fitness.models import Swim


@require_GET
def swims_html(
    request: HttpRequest,
    swim_year: str | None = None,
    swim_month: str | None = None,
    swim_day: str | None = None,
    **_: dict,
) -> render:
    objects = Swim.objects.all()
    if swim_year:
        objects = objects.filter(date__year=swim_year)
    if swim_month:
        objects = objects.filter(date__month=swim_month)
    if swim_day:
        objects = objects.filter(date__day=swim_day)

    if objects.count() == 1:
        return redirect(
            objects.first().get_absolute_url(),
        )

    return render(
        request,
        "fitness/swims.html",
        {
            "base_template": ("partial.html" if request.htmx else "base.html"),
            "page": Paginator(
                object_list=objects.order_by("date"),
                per_page=10,
            ).get_page(
                request.GET.get("page", 1),
            ),
            "breadcrumbs": list(
                filter(
                    lambda x: x is not None,
                    [
                        {
                            "title": "Swims",
                            "url": reverse(
                                "swims_html",
                            ),
                        },
                        {
                            "title": swim_year,
                            "url": reverse(
                                "swims_year",
                                kwargs={
                                    "swim_year": swim_year,
                                },
                            ),
                        }
                        if swim_year
                        else None,
                        {
                            "title": calendar.month_name[int(swim_month)],
                            "url": reverse(
                                "swims_month",
                                kwargs={
                                    "swim_year": swim_year,
                                    "swim_month": swim_month,
                                },
                            ),
                        }
                        if swim_month
                        else None,
                        {
                            "title": ordinal(swim_day),
                            "url": reverse(
                                "swims_day",
                                kwargs={
                                    "swim_year": swim_year,
                                    "swim_month": swim_month,
                                    "swim_day": swim_day,
                                },
                            ),
                        }
                        if swim_day
                        else None,
                    ],
                )
            ),
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "href": request.build_absolute_uri(
                        reverse(
                            "swims_html",
                        ),
                    ),
                },
            ],
        },
    )
