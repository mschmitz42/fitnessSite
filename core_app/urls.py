from django.urls import path
from core_app import views
from django.views.generic.base import TemplateView


app_name = 'core_app'

urlpatterns = [
    path('', views.core_app_index, name='core-app-index'),
    path('home', views.core_app_index, name='home'),
    path('menu', views.core_app_menu, name='menu'),
    path('profile', views.core_app_profile, name='profile'),
    path('upload', views.core_app_file_upload, name='upload'),
    path('under-construction', views.core_app_under_construction, name='under-construction'),
]
