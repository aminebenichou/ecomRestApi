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

# @api_view(['POST'])
# def home(request):
#     return Response({'msg':'hello'}, status=HTTP_200_OK)


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        acc_type = request.query_params.get('accounttype')
        if acc_type == 'client':
            print('client')
            result = []
            for product in self.queryset :
                result.append(
                    {
                        'id': product.id,
                        'title': product.title,
                        'desc': product.description,
                        'price': product.price,
                    }
                )
            return Response(result, status=HTTP_200_OK)
        if acc_type == 'seller':
            print('seller')
            return Response([], status=HTTP_200_OK)
        return Response([], status=HTTP_200_OK)
        


