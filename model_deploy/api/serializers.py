from rest_framework import serializers

class DiabeticTypeSerializer(serializers.Serializer):
    age = serializers.FloatField()
    bs_fast = serializers.FloatField()
    bs_pp = serializers.FloatField()
    plasma_r = serializers.FloatField()
    plasma_f = serializers.FloatField()
    hbA1c = serializers.FloatField()
