from geolocation.models import Provider, ServiceArea
from rest_framework import serializers


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceArea
        fields = '__all__'
