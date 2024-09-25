from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import viewsets
from .models import *
from .serializers import *
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
        

