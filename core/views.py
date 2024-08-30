from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT
)


from .models import (Product,Movements)
from .serializers import(UserSerializer,ProductSerializer,MovementsSerializer,) 



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs): 
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):    
        return super().destroy(request, *args, **kwargs)
    
class ProductViewSet(viewsets.ModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def list(self, request, *args, **kwargs):
        
        product= Product.objects.all()
        serializer=ProductSerializer(product,many=True)
        
        return JsonResponse(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data= request.data
        if not data:
            return JsonResponse('infrome o produto',status=HTTP_400_BAD_REQUEST)
        
        '''id nome preço e movimento '''
        
        
        name= request.data.get('name')
        price= request.data.get('price')
        quantity= request.data.get('quantity')
        
        product= Product.objects.create(
            name=name,
            price=price,
            stock_quantity=quantity
            
        )
        
        Movements.objects.create(
            product=product,
            movement_type= Movements.IN,
            amount = quantity
        )
        
        
        serializer =self.get_serializer(product)
        headers= self.get_success_headers(serializer.data)
        
        return JsonResponse(serializer.data, status=HTTP_201_CREATED, headers=headers)   
        
    def partial_update(self, request, *args, **kwargs): 
        
        name = request.data.get('name')
        if not  name:
            return JsonResponse('infrome o produto',status=HTTP_400_BAD_REQUEST)
        
        pk = self.kwargs.get('pk', None)
        
        editor = Product.objects.filter(pk=pk).update(
            name = name
        )
        product = Product.objects.filter(id=editor).first()
        
        serializer = ProductSerializer(product, many = False)
        
        return JsonResponse(serializer.data, status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):    
        
        product= self.get_object()
        product.delete()
      
        return JsonResponse([], status=HTTP_204_NO_CONTENT)
    
    
class MovementsViewSet(viewsets.ModelViewSet):
    queryset = Movements.objects.all()  
    serializer_class = MovementsSerializer  
    
    def list(self, request, *args, **kwargs):
        
        movement= Movements.objects.all()
        serializer=MovementsSerializer(movement,many=True)
        
        return JsonResponse(serializer.data)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)     

    def partial_update(self, request, *args, **kwargs): 
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):    
        return super().destroy(request, *args, **kwargs)
    
