from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from rest_framework import serializers

from .models import *

#Djoser gives us endpoint for users, need to override the serializer since we are using custom users
class UserCreateSerializer(BaseUserRegistrationSerializer):
        class Meta(BaseUserRegistrationSerializer.Meta):
                model = CustomUser
                fields = ( 
                        "id",
                        "email",
                        "password",
                        "is_business_owner",
                        "is_business_user",
                        "is_consumer_user",
                )

class CompanyBoxSerializer(serializers.ModelSerializer):
        class Meta:
                model = Company
                fields = (
                        "id",
                        "name",
                        "get_description",
                        "get_image",
                        "get_rating",
                        "get_recent_rating",
                )

class LocationSerializer(serializers.ModelSerializer):
        class Meta:
                model = Location
                fields = (
                        "id",
                        "address",
                        "get_region",
                        "company",
                )

class ServiceSerializer(serializers.ModelSerializer):
        class Meta:
                model = Service
                fields = (
                        "id",
                        "name",
                        "parent",
                        "get_companies",
                )
