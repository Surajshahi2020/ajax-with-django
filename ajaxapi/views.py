from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
import json
from ajaxapi.models import Member


# Create your views here.
class MemberCreateAPiView(APIView):
    def post(self,request, *args, **kwargs):
        if not request.body:
            message = {
            "error": "Cannot be blank"
            }
            return JsonResponse(message, status=404)
        else:
            data = json.loads(request.body)
            name = str(data["name"]).strip() if 'name' in data else ''
            email = str(data["email"]).strip() if 'email' in data else ''
            password= str(data["password"]).strip() if 'password' in data else ''
            Member.objects.create(name=name,email=email,password=password)
            message={
                "success":"Ok"
            }
            return JsonResponse(message, status=200)

