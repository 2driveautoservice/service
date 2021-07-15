from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *

from .models import *

class CompanyBoxList(APIView):
    def get(self, request, format=None):
        company_box_list = Company.objects.all()
        serializer = CompanyBoxSerializer(company_box_list, many=True)
        return Response(serializer.data)

class LocationList(APIView):
    def get(self, request, format=None):
        location_list = Location.objects.all()
        serializer = LocationSerializer(location_list, many=True)
        return Response(serializer.data)

class ServiceList(APIView):
    def get(self, request, format=None):
        service_list = Service.objects.all()
        serializer = ServiceSerializer(service_list, many=True)
        return Response(serializer.data)
    




    
