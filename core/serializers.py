from rest_framework import serializers
from .models import (
   User,
   Product,
   Movements, 
   
   ) 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'name','price', 

class MovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movements
        fields = '__all__'  



        
    