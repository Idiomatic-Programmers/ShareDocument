from django.urls import path, include
from . import views


urlpatterns = [
    path('profile/', views.add_document, name="accounts_add_document"),
    path('share/<str:key>/', views.share_document, name="accounts_share_document"),
    path('delete/<str:key>/', views.delete_document, name="accounts_delete_document"),
    path('documents/', views.all_documents, name="all_documents"),
    path('auth/', include('django.contrib.auth.urls')),
]
