from django.urls import path
from .views import GoogleDriveUpload

urlpatterns = [
    path('', GoogleDriveUpload.as_view(), name='google_drive_upload'),
]
