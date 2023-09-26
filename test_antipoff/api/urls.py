from django.urls import path

from . import views


app_name = "api"


urlpatterns = [
    path("query/", views.query, name="query"),
    path("result/", views.result, name="result"),
    path("ping/", views.ping, name="ping"),
    path("history/", views.history, name="history"),
]
