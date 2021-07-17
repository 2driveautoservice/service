from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *

from .models import *

class CompanyBoxList(APIView):
    def get(self, request, format=None):
        company_box_list = Company.objects.all().order_by('name')
        serializer = CompanyBoxSerializer(company_box_list, many=True)
        return Response(serializer.data)

class LocationList(APIView):
    def get(self, request, format=None):
        location_list = Location.objects.all().order_by('region__name')
        serializer = LocationSerializer(location_list, many=True)
        return Response(serializer.data)

class ServiceList(APIView):
    def get(self, request, format=None):
        service_list = Service.objects.all().order_by('name')
        serializer = ServiceSerializer(service_list, many=True)
        return Response(serializer.data)
    




    
