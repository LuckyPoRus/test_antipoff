<h1 align="center">Test_antipoff</h1>

## Описание проекта
Сервис принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем отдаёт результат запроса. Внешний сервер может ответить `true` или `false`.
Данные запроса на сервер и ответ с внешнего сервера должны быть сохраненяются в БД.
Сервис содержит следующие эндпоинты:
"/query" - для получения запроса
“/result" - для отправки результата
"/ping" - проверка, что  сервер запустился
“/history” - для получения истории запросов


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
5. Создание образа бэкенда:
```
cd ./test_antipoff/
docker build -t <your_username>/<test_antipoff> .
```
6. Запуск контейнеров:
```
docker-compose up -d
```
7. После успешного запуска контейнеров необходимо выполнить миграции, <br/>
создать суперпользователя и собрать статику:
```
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
```
8. Проверить работу сервиса:
[http://127.0.0.1](http://127.0.0.1)
