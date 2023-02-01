from django.urls import path, include
from tracker import views
from rest_framework.routers import DefaultRouter


app_name = 'tracker'


router = DefaultRouter()
router.register(r"measurements", views.MeasurementViewSet, "measurement")


urlpatterns = [
    path('', views.tracker_index, name='tracker'),
    path('api/', include(router.urls)),
]
