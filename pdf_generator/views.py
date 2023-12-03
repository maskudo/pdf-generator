import os
from typing import Any

from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from pdf_generator.helpers import generate_pdf, get_all_pdfs

REQUIRED_FIELDS = ["name", "address", "email", "phone"]
if not os.path.exists(settings.MEDIA_ROOT):
    os.makedirs(settings.MEDIA_ROOT)


@api_view(["GET", "POST"])
def index(request: Request):
    if request.method == "GET":
        pdfs = get_all_pdfs()
        return Response({"pdfs": pdfs})

    data: dict[Any, Any] = request.data
    has_required_fields = all([k in data.keys() for k in REQUIRED_FIELDS])
    if not has_required_fields:
        return Response(
            {"message": "must have fields name, address, email, phone"}, 400
        )
    elif len(data.keys()) > 10:
        return Response(
            {"message": "too many fields. can support a maximum of 10."}, 400
        )

    pdf_path = generate_pdf(data)
    return Response({"pdf": pdf_path}, 201)


@api_view(["GET"])
def get_pdf(request: Request, pdf_id: str):
    try:
        output_filename = os.path.join(settings.MEDIA_ROOT, pdf_id)
        with open(output_filename, "rb") as f:
            response = HttpResponse(f, content_type="application/pdf")
            response["Content-Disposition"] = "attachment; filename=NameOfFile"
            return response
    except:
        return Response({"message": "Resource not found"}, 404)
