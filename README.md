Социальная сеть для публикации постов
=====
Проект развёрнут на хостинге и доступен по адресу http://188.120.253.26/

Описание проекта
----------

Социальная сеть для авторов и подписчиков. Пользователи могут:
1) подписываться на избранных авторов
2) оставлять и удалять комментари к постам
3) добавлять новые посты на главной странице и в тематических группах
4) прикреплять изображения к публикуемым постам. 
5) осталять лайки на постах авторов

В данном проекте реализованы следующие требования:
----------
1. Аутентификация пользователя по JWT-токенам
2. Подтверждение регистрации/Восстановления пароля по почте
3. Кастомная модель User и кастомный бэкенд аутентификации(см authenricate/backends.py)
4. Профиль пользователя(автоматическая генерация при регистрации 
   пользователя при помощи сигнала (см authenricate/signals.py))
5. Кастомный permissions(см social/permissions.py)
6. CORS настройки 
7. Документация:
    Swagger: http://188.120.253.26/swagger/ 
    Redoc: http://188.120.253.26/redoc/
8. База данных PostgresSQL

Системные требования
----------
* Python 3.10
* Works on Linux, Windows, macOS, BSD

Стек технологий
----------
* Python 3.10
* Django 4.1
* Django REST Framework 3.14.0
* Postgres

Установка проекта из репозитория (Linux и macOS)
----------

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
cd social_network_API
```
2. Cоздать и активировать виртуальное окружение:
```bash
python3.10 -m venv env

source env/bin/activate
```
3. Установить зависимости из файла ```requirements.txt```:
```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
pip install psycopg2-binary

4. Произвести настройки базы данных:
```bash
sudo -u postgres psql

CREATE DATABASE social_db WITH ENCODING='UTF-8';
CREATE USER social_user WITH PASSWORD 'ErW12ss3';
ALTER ROLE social_user SET client_encoding TO 'utf8';
ALTER ROLE social_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE social_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE social_db TO social_user;
\q

5. Выполнить миграции:
```bash
cd social_network_API

python manage.py migrate
```
6. Запустить проект (в режиме сервера Django):
```bash
python manage.py runserver
```
