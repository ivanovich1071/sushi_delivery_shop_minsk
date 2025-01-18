from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]
