from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.document_security, name="viewer_security"),
    path('document/<str:key>', views.document_viewer, name="viewer_document"),
]
