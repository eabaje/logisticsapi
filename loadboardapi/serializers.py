# convert api results to json/xml


from rest_framework import serializers
from .models import *

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drivers
        field='__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Companys
        field='__all__'

class AssignDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assigndrivers
        field='__all__'

class CarriersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carriers
        field='__all__'

class InsurancesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Insurances
        field='__all__'


class MediasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medias
        field='__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        field='__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payments
        field='__all__'


class ShipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shipments
        field='__all__'


class ShipmentsinterestedsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shipmentsinteresteds
        field='__all__'


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subscriptions
        field='__all__'


class TracksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tracks
        field='__all__'


class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trips
        field='__all__'


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Roles
        field='__all__'



class UserrolesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userroles
        field='__all__'


class UsersubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usersubscriptions
        field='__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        field='__all__'


class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicles
        field='__all__'


