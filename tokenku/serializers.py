from rest_framework import serializers
from .models import WsFeeder

class WsFeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = WsFeeder
        fields = '__all__'