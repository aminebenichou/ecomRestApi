from django.shortcuts import render 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import viewsets, status
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.models import Group
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Client, User  
from .serializers import ClientSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,logout

# Create your views here.
# abcdefgh
# hello

# @api_view(['GET'])
# def home(request):
#     return Response({'msg':'hello'}, status=HTTP_200_OK)


# class Home(viewsets.ModelViewSet):
#     queryset = Client.objects.all()      # Récupère tous les objets Client dans la base de données
#     serializer_class = ClientSerializer
#     def list(self, request, *args, **kwargs):
#         result = Client.objects.all()
#         print(result)
#         resulttwo = []
#         for item in result:
#             resulttwo.append({      # Ajoute un dictionnaire avec des champs spécifiques à la liste resulttwo
#                 'id':item.id,
#                 'name':item.name,
#                 'total orders':'hello'
#             })
#         return Response(resulttwo, status=HTTP_200_OK)


def assign_to_group(user, role):
    if role == 'client':
        group = Group.objects.get(name='Clients')
    elif role == 'seller':
        group = Group.objects.get(name='Sellers')
    user.groups.add(group)

# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def create(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()            
#             token = Token.objects.create(user=user) 
#             return Response({
#                 'user': serializer.data,
#                 'token': token.key  
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ClientView(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

#     def create(self, request, *args, **kwargs):
#         user_data = request.data.get('user')
#         password = request.data.get('password')
#         if user_data:  
#             user_serializer = UserSerializer(data=user_data)
#             if user_serializer.is_valid():
#                 user = user_serializer.save() 
#                 user.set_password(password)                
#                 token = Token.objects.create(user=user)
#                 assign_to_group(user, role='client')

                
#                 client_data = request.data.copy()
#                 client_data['user'] = user.id  
                
#                 client_serializer = self.get_serializer(data=client_data)
#                 if client_serializer.is_valid():
#                     client_serializer.save()  
#                 return Response({
#                 'user': client_serializer.data,
#                 'token': token.key  
#             }, status=status.HTTP_201_CREATED)
            
        
#         return Response({"user": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# class SellerView(viewsets.ModelViewSet):
#     queryset= Seller.objects.all()
#     serializer_class=SellerSerializer
#     def create(self, request, *args, **kwargs):
#     #     return super().create(request, *args, **kwargs)
#     # def createSeller(self,request):
#         user_data = request.data.get('user')
#         password = user_data('password')
#         if user_data:
#             user_serializer = UserSerializer(data=user_data)
#             if user_serializer.is_valid():
#                 user = user_serializer.save()  
#                 user.set_password(password)  
#                 user.save() 
#                 token = Token.objects.create(user=user)
#                 assign_to_group(user, role='seller')
#                 seller_data = request.data.copy()
#                 seller_data['user'] = user.id
#                 seller_serializer = self.get_serializer(data=seller_data)
#                 if seller_serializer.is_valid():
#                     seller_serializer.save()
#                     return Response({
#                         'seller': seller_serializer.data,
#                         'token': token.key  
#                     }, status=status.HTTP_201_CREATED)
#                 return Response(seller_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
#             return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         return Response({'error': 'User data is required.'}, status=status.HTTP_400_BAD_REQUEST)


# def loginView( request):
#         username = request.data.get('username') 
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             token = Token.objects.get_or_create(user=user)
#             return Response({
#                 'token': token.key,  
#                 'user_id': user.id, 
#                 'username': user.username, 
#             }, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
# def logoutView(request):
#     logout(request)
#     return
def choice(request):
    pass
    


          
              
      
        
    


    
        

        
          
          
        
    
        

