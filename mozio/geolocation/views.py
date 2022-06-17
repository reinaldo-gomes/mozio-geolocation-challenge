from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from geolocation.models import Provider, ServiceArea
from geolocation.serializers import ProviderSerializer, ServiceAreaSerializer
from shapely.geometry import Point, Polygon


@api_view(['GET'])
def overlapping_areas(request):
    if request.method == 'GET':
        latitude = request.query_params.get('lat')
        longitude = request.query_params.get('lng')

        if not latitude or not longitude:
            return Response({'msg': 'lat/lng must be set'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            point = Point(float(latitude), float(longitude))
        except ValueError:
            return Response({'msg': 'lat/lng must be integer or decimal'}, status=status.HTTP_400_BAD_REQUEST)

        queryset = []
        for item in ServiceArea.objects.all():
            if not isinstance(item.geolocation, dict):
                continue

            coordinates = item.geolocation.get('geometry', {}).get('coordinates', [])
            if point.within(Polygon(coordinates)):
                queryset.append({
                    'provider': item.provider.name,
                    'name': item.name,
                    'price': item.price,
                    'geolocation': item.geolocation
                })

        return Response(queryset)


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('-created_at')
    serializer_class = ProviderSerializer
    #permission_classes = [permissions.IsAuthenticated]


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all().order_by('-created_at')
    serializer_class = ServiceAreaSerializer
    #permission_classes = [permissions.IsAuthenticated]
