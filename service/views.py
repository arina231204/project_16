from django.db.models import Avg
from rest_framework import viewsets, mixins, status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, action
from rest_framework.views import APIView

from account.models import Profile
from service.models import Taxi, Order, StatusDriver, StatusType
from service.permissions import IsAuthorPermission, IsOwnerOrReadOnly, IsNotAuthorPermission
from service.serializers import TaxiSerializer, OrderSerializer, StatusDriverSerializer, StatusTypeSerializer


class TaxiListAPIView(viewsets.ModelViewSet):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = [IsAuthorPermission, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsNotAuthorPermission, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class StatusTypeViewSet(viewsets.ModelViewSet):
    queryset = StatusType.objects.all()
    serializer_class = StatusTypeSerializer


class StatusDriverViewSet(viewsets.ModelViewSet):
    queryset = StatusDriver.objects.all()
    serializer_class = StatusDriverSerializer

    @action(detail=True, methods=['POST'])
    def rate_driver(self, request, pk=None):
        driver = self.get_object()
        driver.rating = (driver.rating + request.data.get('rating')) / 2
        driver.save()
        return Response({'status': 'Driver rating updated'})
