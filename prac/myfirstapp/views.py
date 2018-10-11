# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import  APIView
from .models import Stock
from .serializers import StockSerializers
from rest_framework.response import Response
from rest_framework import status


class Stocklist(APIView):

    def get(self,request):
        stocks = Stock.objects.all()
        serializers = StockSerializers(stocks,many=True)
        return  Response(serializers.data)
    def post(self,request):
        serializers = StockSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#
# creating new views for new models called users




