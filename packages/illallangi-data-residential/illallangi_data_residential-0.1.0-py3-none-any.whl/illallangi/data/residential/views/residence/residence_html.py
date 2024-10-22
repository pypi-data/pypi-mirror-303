from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.residential.models import Residence


@require_GET
def residence_html(
    request: HttpRequest,
    residence_slug: str,
    **_: dict,
) -> render:
    objects = Residence.objects.filter(slug=residence_slug)

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple residences found for slug",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "residential/residence.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Residences",
                        "url": reverse(
                            "residences_html",
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
        content="Residence not found",
    )
