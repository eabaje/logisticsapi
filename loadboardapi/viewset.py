#

from rest_framework import viewsets
from . import models
from . import serializers

class DriverViewSet(viewsets.ModelViewSet):
    queryset=models.Drivers.objects.all()
    serializer_class=serializers.DriverSerializer

class AssignDriverViewSet(viewsets.ModelViewSet):
    queryset=models.Assigndrivers.objects.all()
    serializer_class=serializers.DriverSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=models.Companys.objects.all()
    serializer_class=serializers.DriverSerializer

class CarrierViewSet(viewsets.ModelViewSet):
    queryset=models.Carriers.objects.all()
    serializer_class=serializers.DriverSerializer

class AssignShipmentViewSet(viewsets.ModelViewSet):
    queryset=models.Assignshipments.objects.all()
    serializer_class=serializers.DriverSerializer

class InsuranceViewSet(viewsets.ModelViewSet):
    queryset=models.Insurances.objects.all()
    serializer_class=serializers.DriverSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset=models.Medias.objects.all()
    serializer_class=serializers.DriverSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset=models.Orders.objects.all()
    serializer_class=serializers.DriverSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset=models.Payments.objects.all()
    serializer_class=serializers.DriverSerializer

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset=models.Shipments.objects.all()
    serializer_class=serializers.DriverSerializer

class ShipmentsinterestedViewSet(viewsets.ModelViewSet):
    queryset=models.Shipmentsinteresteds.objects.all()
    serializer_class=serializers.DriverSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset=models.Subscriptions.objects.all()
    serializer_class=serializers.DriverSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset=models.Tracks.objects.all()
    serializer_class=serializers.DriverSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset=models.Trips.objects.all()
    serializer_class=serializers.DriverSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset=models.Roles.objects.all()
    serializer_class=serializers.DriverSerializer

class UserroleViewSet(viewsets.ModelViewSet):
    queryset=models.Userroles.objects.all()
    serializer_class=serializers.DriverSerializer

class UsersubscriptionViewSet(viewsets.ModelViewSet):
    queryset=models.Usersubscriptions.objects.all()
    serializer_class=serializers.DriverSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=models.Users.objects.all()
    serializer_class=serializers.DriverSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset=models.Vehicles.objects.all()
    serializer_class=serializers.DriverSerializer


