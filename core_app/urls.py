from django.urls import path, include
from core_app import views
from django.views.generic.base import TemplateView
from rest_framework.routers import DefaultRouter


app_name = 'core_app'


router = DefaultRouter()
router.register(r"profiles", views.ProfileViewSet, "profiles")


urlpatterns = [
    path('', views.core_app_index, name='core-app-index'),
    path('home', views.core_app_index, name='home'),
    path('menu', views.core_app_menu, name='menu'),
    path('profile', views.core_app_profile, name='profile'),
    path('client', views.core_app_client, name='client'),
    path('measurement-upload', views.core_app_measurement_file_upload, name='measurement-upload'),
    path('macro-upload', views.core_app_macro_file_upload, name='macro-upload'),
    path('under-construction', views.core_app_under_construction, name='under-construction'),
    path('api/', include(router.urls)),
]
