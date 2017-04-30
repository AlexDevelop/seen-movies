from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from biking.models import BikeRide
from biking.serializers import BikeRideSerializer


class BikeRideViewSet(viewsets.ViewSet, ModelViewSet):
    serializer_class = BikeRideSerializer
    queryset = BikeRide.objects.all()