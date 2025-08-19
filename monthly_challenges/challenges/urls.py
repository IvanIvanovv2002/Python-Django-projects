from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:month>', views.month_view_int),
    path('<str:month>', views.month_view, name='month-challenge'),
]
