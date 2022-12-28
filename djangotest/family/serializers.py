from rest_framework import serializers
from .models import Family, Child

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ("name", "parent_id")

class FamilySerializer(serializers.ModelSerializer): 
    child_fields = ChildSerializer(many=True)
    class Meta:
        model = Family        
        fields = ("id", "name", "child_fields")




