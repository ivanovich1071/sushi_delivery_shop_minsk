from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('catalog/', views.catalog, name='catalog'),  # Каталог товаров
    path('login/', views.login_view, name='login'),  # Страница входа
    path('register/', views.register, name='register'),  # Страница регистрации
]
