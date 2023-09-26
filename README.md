<h1 align="center">Test_antipoff</h1>

## Описание проекта
Сервис принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем отдаёт результат запроса. Внешний сервер может ответить `true` или `false`.
Данные запроса на сервер и ответ с внешнего сервера сохраняются в БД.<br/>
Сервис содержит следующие эндпоинты:<br/>
"/query" - для получения запроса<br/>
“/result" - для отправки результата<br/>
"/ping" - проверка, что  сервер запустился<br/>
“/history” - для получения истории запросов<br/>


## Используемые технологии:
- Django - 4.2.5
- Django Rest Framework - 3.14.0
- Python 3.10.10
- PostgreSQL
- Docker
- Gunicorn
- Nginx

## Как запустить проект:
### Локально:
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:LuckyPoRus/test_antipoff.git
```
2. Переход в директорию и активация виртуального окружения:
```
cd test_antipoff
```
3. Создание и активация виртуального окружения:
```
python -m venv venv
source venv/scripts/activate
```
4. Обновление pip и установка зависимостей:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
5. Создать файл .env и добавить в него следующую информацию
```
SECRET_KEY=test
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=test
DB_USER=test
DB_PASSWORD=test1234
DB_HOST=test
DB_PORT=5432
POSTGRES_PASSWORD=test1234
POSTGRES_HOST=test
POSTGRES_PORT=5432
```
6. Создание образа бэкенда:
```
cd ./test_antipoff/
docker build -t <your_username>/<test_antipoff> .
```
7. Запуск контейнеров:
```
docker-compose up -d
```
8. После успешного запуска контейнеров необходимо выполнить миграции, <br/>
создать суперпользователя и собрать статику:
```
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
```
9. Проверить работу сервиса:
[http://127.0.0.1](http://127.0.0.1)

## Запрос с вводными данными
- POST
```
http://127.0.0.1:8000/api/query/
{
    "cadastre_number" : 123, 
    "latitude" : 123.123,
    "longitude" : 123.123
}
```
## Запрос на внешний сервер и получение результата
- POST
```
http://127.0.0.1:8000/api/result/
{
    "cadastre_number" : 123
}
```
## Проверка работоспособности сервера
- GET
```
http://127.0.0.1:8000/api/ping/
```
## Получение истории запросов
- GET
```
http://127.0.0.1:8000/api/history/
```
## Документация
- GET
```
http://127.0.0.1:8000/redoc/
```
**Автор проекта:**<br/>
**Павел** - https://github.com/LuckyPoRus<br/>
