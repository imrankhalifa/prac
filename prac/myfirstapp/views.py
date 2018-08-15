# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import  APIView
from .models import Stock
from .serializers import StockSerializers
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
# Create your views here.


# class Stocklist(APIView):
#
#
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'stock_list.html'
#
#      def get(self, request):
#          queryset = Stock.objects.all()
#          return Response({'Stocks':queryset})

class StockDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'stock_detail.html'

    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        serializer = StockSerializers(stock)
        return Response({'serializer': serializer, 'Stock': Stock})

    def post(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        serializer = StockSerializers(stock, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'Stock': Stock})
        serializer.save()




    # def get(self,request):
    #     stocks = Stock.objects.all()
    #     serializers = StockSerializers(stocks,many=True)
    #     return  Response(serializers.data)
    # def post(self,request):
    #     serializers = StockSerializers(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data,status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


