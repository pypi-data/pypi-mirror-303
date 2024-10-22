import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.mastodon.models import Status


@require_GET
def statuses_html(
    request: HttpRequest,
    status_year: str | None = None,
    status_month: str | None = None,
    status_day: str | None = None,
    **_: dict,
) -> render:
    objects = Status.objects.all()
    if status_year:
        objects = objects.filter(datetime__year=status_year)
    if status_month:
        objects = objects.filter(datetime__month=status_month)
    if status_day:
        objects = objects.filter(datetime__day=status_day)

    if objects.count() == 1:
        return redirect(
            objects.first().get_absolute_url(),
        )

    return render(
        request,
        "mastodon/statuses.html",
        {
            "base_template": ("partial.html" if request.htmx else "base.html"),
            "page": Paginator(
                object_list=objects.order_by("datetime"),
                per_page=10,
            ).get_page(
                request.GET.get("page", 1),
            ),
            "breadcrumbs": list(
                filter(
                    lambda x: x is not None,
                    [
                        {
                            "title": "Statuses",
                            "url": reverse(
                                "statuses_html",
                            ),
                        },
                        {
                            "title": status_year,
                            "url": reverse(
                                "statuses_year",
                                kwargs={
                                    "status_year": status_year,
                                },
                            ),
                        }
                        if status_year
                        else None,
                        {
                            "title": calendar.month_name[int(status_month)],
                            "url": reverse(
                                "statuses_month",
                                kwargs={
                                    "status_year": status_year,
                                    "status_month": status_month,
                                },
                            ),
                        }
                        if status_month
                        else None,
                        {
                            "title": ordinal(status_day),
                            "url": reverse(
                                "statuses_day",
                                kwargs={
                                    "status_year": status_year,
                                    "status_month": status_month,
                                    "status_day": status_day,
                                },
                            ),
                        }
                        if status_day
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
                            "statuses_html",
                        ),
                    ),
                },
            ],
        },
    )
