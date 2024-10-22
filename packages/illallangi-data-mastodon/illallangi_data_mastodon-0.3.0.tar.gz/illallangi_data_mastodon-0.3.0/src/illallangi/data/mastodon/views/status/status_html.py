import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.mastodon.models import Status


@require_GET
def status_html(
    request: HttpRequest,
    status_slug: str,
    **_: dict,
) -> render:
    objects = Status.objects.filter(sqid=status_slug)

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple statuses found for slug",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "mastodon/status.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Statuses",
                        "url": reverse(
                            "statuses_html",
                        ),
                    },
                    {
                        "title": obj.datetime.year,
                        "url": reverse(
                            "statuses_year",
                            kwargs={
                                "status_year": str(obj.datetime.year).zfill(4),
                            },
                        ),
                    },
                    {
                        "title": calendar.month_name[obj.datetime.month],
                        "url": reverse(
                            "statuses_month",
                            kwargs={
                                "status_year": str(obj.datetime.year).zfill(4),
                                "status_month": str(obj.datetime.month).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": ordinal(obj.datetime.day),
                        "url": reverse(
                            "statuses_day",
                            kwargs={
                                "status_year": str(obj.datetime.year).zfill(4),
                                "status_month": str(obj.datetime.month).zfill(2),
                                "status_day": str(obj.datetime.day).zfill(2),
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
        content="Status not found",
    )
