from django.urls import path
from core_app import views
from django.views.generic.base import TemplateView


app_name = 'core_app'

urlpatterns = [
    path('', views.core_app_index, name='core-app-index'),
    path('home', views.core_app_index, name='home'),
    path('dashboard', views.core_app_dashboard, name='dashboard'),
    path('under-construction', views.core_app_under_construction, name='under-construction'),
]
