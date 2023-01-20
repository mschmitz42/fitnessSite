from django.urls import path
from coreApp import views

app_name = 'coreApp'

urlpatterns = [
    path('', views.coreApp_index, name='coreApp_index'),
    path('home', views.coreApp_index, name='home'),
    # path('about', views.core_about, name='core_about'),
    # path('scheduler', views.core_scheduler, name='core_scheduler'),
    # path('profile', views.core_profile, name='core_profile'),
]
