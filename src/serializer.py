from rest_framework import serializers
from .models import NetworkMobile


class NetworkMobilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkMobile

    def to_representation(self, instance):
        operators = []
        if instance.g2:
            operators.append('2G')
        if instance.g3:
            operators.append('3G')
        if instance.g4:
            operators.append('4G')
        if not operators:
            return {instance.operator.name: "No network coverage"}
        return {
            instance.operator.name: operators
        }
