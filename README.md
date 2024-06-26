# Django Google Drive Uploader

Этот проект предоставляет API для загрузки файлов в Google Drive с использованием Django и Google API.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Yanina-t/API_NOVA_test.git

    cd yourrepo
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Настройте файл `settings.py`:
    - Добавьте ваш `SECRET_KEY`.
    - Настройте `ALLOWED_HOSTS`.

5. Запустите миграции базы данных:
    ```bash
    python manage.py migrate
    ```

6. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

## Развертывание на Heroku

1. Создайте приложение на Heroku:
    ```bash
    heroku create yourapp
    ```

2. Добавьте buildpack для Python:
    ```bash
    heroku buildpacks:add heroku/python
    ```

3. Настройте переменные окружения:
    ```bash
    heroku config:set SECRET_KEY='your-secret-key'
    heroku config:set DEBUG='False'
    heroku config:set DB_NAME='your-db-name'
    heroku config:set DB_USER='your-db-user'
    heroku config:set DB_PASSWORD='your-db-password'
    heroku config:set DB_HOST='your-db-host'
    heroku config:set DB_PORT='5432'
    ```

4. Разверните приложение:
    ```bash
    git push heroku master
    ```

5. Примените миграции базы данных:
    ```bash
    heroku run python manage.py migrate
    ```

## Использование API

Отправьте POST запрос параметрами:
- `name`: Название файла
- `data`: Текстовое содержимое файла

## Пример запроса

```bash
curl -X POST https://yourapp.herokuapp.com/api/upload/ -H "Content-Type: application/json" -d '{"name": "example.txt", "data": "Hello, world!"}'
