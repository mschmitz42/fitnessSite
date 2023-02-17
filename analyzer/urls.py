from django.urls import path
from analyzer import views


app_name = 'analyzer'


urlpatterns = [
    path('', views.analyzer_index, name='analyzer'),
]
