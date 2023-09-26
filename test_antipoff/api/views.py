import time
import random

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cadastre.models import Result
from .serializers import QuerySerializer, ResultSerializer


# Получаем и сохраняем в БД запрос с вводными данными
@api_view(["POST"])
def query(request):
    serializer = QuerySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Отправка запроса с кадастровым номером на сервер и получение результата
@api_view(["POST"])
def result(request):
    serializer = ResultSerializer(data=request.data)
    if serializer.is_valid():
        result = random.choice([True, False])
        time.sleep(60)
        serializer.save(result=result)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Проверка работоспособности сервера
@api_view(["GET"])
def ping(request):
    message = "Сервер работает!"
    return Response(message, status=status.HTTP_200_OK)


# Получаем историю запросов
@api_view(["GET"])
def history(request):
    history = Result.objects.all().order_by("-cadastre_number__create_date")
    serializer = ResultSerializer(history, many=True)
    return Response(serializer.data)
