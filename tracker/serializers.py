from rest_framework import serializers
from .models import Measurement, Macro


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"


class MacroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macro
        fields = "__all__"

