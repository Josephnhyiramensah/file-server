from django.urls import path, include
from . import views, api_views

urlpatterns = [
    # HTML views
    path('', views.document_list, name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('send/<int:document_id>/', views.send_file_email, name='send_file_email'),
    path('download/<int:document_id>/', views.download_document, name='download_document'),

    # API views
    path('api/users/', api_views.UserCreate.as_view(), name='user_create'),
    path('api/documents/', api_views.DocumentList.as_view(), name='document_list_api'),
    path('api/documents/<int:pk>/', api_views.DocumentDetail.as_view(), name='document_detail_api'),
    path('other_app/', include('other_app.urls')),
]