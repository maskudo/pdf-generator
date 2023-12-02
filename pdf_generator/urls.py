from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:pdf_id>", views.get_pdf, name="get_pdf"),
]
