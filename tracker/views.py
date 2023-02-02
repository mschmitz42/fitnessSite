from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, AllowAny
from .models import Measurement
from .serializers import MeasurementSerializer
from datetime import datetime, timedelta


def tracker_index(request):
    return render(request, 'tracker/index.html')


@api_view(["GET"])
def get_measurements(request):
    measurements = Measurement.objects.all()
    serializer = MeasurementSerializer(measurements, many=True)
    content = {
        "measurements": serializer.data,
    }

    return Response(content)


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        age = int(self.request.query_params.get("age", 365))
        user_id = int(self.request.query_params.get("user", self.request.user.id))
        start_date = datetime.now()-timedelta(days=age)

        qs = Measurement.objects.filter(user_id=user_id, date__gte=start_date).order_by('date', 'id')

        return qs



