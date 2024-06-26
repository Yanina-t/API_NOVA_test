from django.shortcuts import render
from rest_framework.views import APIView
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io
import os
import json

# Загрузка переменной среды GOOGLE_CREDENTIALS из файла .env
GOOGLE_CREDENTIALS = os.getenv('GOOGLE_CREDENTIALS')
SCOPES = ['https://www.googleapis.com/auth/drive']


# Проверка наличия переменной среды GOOGLE_CREDENTIALS
if not GOOGLE_CREDENTIALS:
    raise ValueError("GOOGLE_CREDENTIALS environment variable is not set")

# Преобразовать строку JSON в словарь
google_credentials_dict = json.loads(GOOGLE_CREDENTIALS)

# Создание объекта credentials из JSON-строки
credentials = service_account.Credentials.from_service_account_info(
    google_credentials_dict, scopes=SCOPES)

service = build('drive', 'v3', credentials=credentials)


class GoogleDriveUpload(APIView):
    template_name = 'myapp/base.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.data.get('name')
        data = request.data.get('data')

        if not name or not data:
            return render(request, self.template_name, {'error': 'Missing name or data'})

        # Используем BytesIO для создания временного файла в памяти
        file_stream = io.BytesIO(data.encode('utf-8'))

        file_metadata = {
            'name': name,
            'parents': ['1aGsG4u5oL7dd2o5nOL-hESJ8wQm1l2QD']  # Замените на ваш ID папки, если необходимо
        }
        media = MediaIoBaseUpload(file_stream, mimetype='text/plain')

        try:
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            return render(request, self.template_name, {'success': True, 'file_id': file.get('id')})
        except Exception as e:
            return render(request, self.template_name, {'error': str(e)})
