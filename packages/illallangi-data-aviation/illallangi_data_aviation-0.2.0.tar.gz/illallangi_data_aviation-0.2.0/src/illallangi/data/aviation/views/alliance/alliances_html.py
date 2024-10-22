from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.aviation.models import Alliance


@require_GET
def alliances_html(
    request: HttpRequest,
    **_: dict,
) -> render:
    objects = Alliance.objects.all()

    if objects.count() == 1:
        return redirect(
            objects.first().get_absolute_url(),
        )

    return render(
        request,
        "aviation/alliances.html",
        {
            "base_template": ("partial.html" if request.htmx else "base.html"),
            "page": Paginator(
                object_list=objects.order_by("name"),
                per_page=10,
            ).get_page(
                request.GET.get("page", 1),
            ),
            "breadcrumbs": [
                {
                    "title": "Alliances",
                    "url": reverse(
                        "alliances_html",
                    ),
                },
            ],
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "href": request.build_absolute_uri(
                        reverse(
                            "alliances_html",
                        ),
                    ),
                },
            ],
        },
    )
