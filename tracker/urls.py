from django.urls import path, include
from tracker import views
from rest_framework.routers import DefaultRouter


app_name = 'tracker'


router = DefaultRouter()
router.register(r"measurements", views.MeasurementViewSet, "measurement")
router.register(r"macros", views.MacroViewSet, "macro")


urlpatterns = [
    path('', views.tracker_index, name='tracker'),
    path('api/', include(router.urls)),
]
