from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from django.http import HttpResponse
from .serializers import *
# Create your views here.



class getlist(APIView):

    def get(self,request):
        all = number.objects.all()
        serializer = NumberSerializer(all, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(request.data)


