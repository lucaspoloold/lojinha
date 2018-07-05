from django.urls import path

from lojinha.core import views

urlpatterns = [
    path('', views.home, name="root"),
    path('contato/', views.contato, name="contato")
]
