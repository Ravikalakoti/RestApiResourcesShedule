from django.shortcuts import render
from .serializers import MySerializer
from .models import MyResource
from rest_framework import viewsets
# Create your views here.
class MyViewSet(viewsets.ModelViewSet):
    queryset = MyResource.objects.all()
    serializer_class = MySerializer