from django.shortcuts import render
from .models import Family, Child
from rest_framework import viewsets
from .serializers import FamilySerializer, ChildSerializer

class familyViewset(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class =  FamilySerializer


class ChildViewset(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
