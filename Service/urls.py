from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('url/done/', views.done, name="done"),
    path('<str:code>', views.route, name="route")
]