from django.urls import path, include
from inicio import views

urlpatterns = [
    path('', views.inicio, name='inicio')
]
