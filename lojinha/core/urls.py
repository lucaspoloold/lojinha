from django.urls import path

from lojinha.core import views

urlpatterns = [
    path('', views.home),
    path('contato/', views.contato)
]
