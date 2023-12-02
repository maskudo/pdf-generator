import os
import threading
from typing import Any, List

from django.conf import settings
from reportlab.pdfgen import canvas
from rest_framework.fields import uuid

DELETE_AFTER_SECONDS = 60 * 60


def generate_pdf(data: dict[Any, Any]) -> str:
    pdf_filename = f"{uuid.uuid4().hex}.pdf"
    output_filename = os.path.join(settings.MEDIA_ROOT, pdf_filename)
    logo_file = os.path.join(settings.BASE_DIR, "static", "logo.png")
    c = canvas.Canvas(output_filename)
    c.drawImage(logo_file, 270, 720, height=100, width=100)
    y_pos = 640
    for key, value in data.items():
        c.drawString(120, y_pos, f"{key}: {value}")
        y_pos -= 20
    c.save()
    threading.Timer(DELETE_AFTER_SECONDS, delete_pdf, args=[output_filename]).start()
    return pdf_filename


def delete_pdf(path: str):
    os.remove(path)


def get_all_pdfs() -> List[str]:
    return [file for file in os.listdir(settings.MEDIA_ROOT) if file.endswith(".pdf")]
