from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.aviation.models import Alliance


@require_GET
def alliance_html(
    request: HttpRequest,
    alliance_slug: str,
    **_: dict,
) -> render:
    objects = Alliance.objects.filter(slug=alliance_slug)

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple alliances found for slug",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "aviation/alliance.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Alliances",
                        "url": reverse(
                            "alliances_html",
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
        content="Alliance not found",
    )
