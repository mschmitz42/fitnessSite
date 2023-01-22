from django.urls import path
from core_app import views

app_name = 'core_app'

urlpatterns = [
    path('', views.core_app_index, name='core-app-index'),
    path('home', views.core_app_index, name='home'),
]
