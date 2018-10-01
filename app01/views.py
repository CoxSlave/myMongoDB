from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app01.models import User
from django.shortcuts import HttpResponse
from mongoengine import connect


class home(APIView):
    def post(self,request):
        connect('project1')
        connect('project1', host='mongodb://localhost:27017/test_database')
        User.objects.create(name="cox",age=12)

        return HttpResponse("mpngodb")