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
        
class MemberGetAPiView(APIView):
    def get(self,request):
        member_data = []
        memdata = Member.objects.all()
        for data in memdata:
            member_data.append({
                    "id": data.id,
                    "name": data.name,
                    "email": data.email,
                    "password": data.password
                })
        message={
            "success":"Ok",
            "data":member_data
        }
        return JsonResponse(message, status=200) 
    
class MemberPutAPiView(APIView):
    def put(self,request,pk):
        data = json.loads(request.body)
        edit = Member.objects.get(id=pk)
        edit.name=data["name"]
        edit.email=data["email"]
        edit.password=data["password"]
        edit.save()
        message={"success":"Ok",
                "data": {
                        "id": edit.id,
                        "name":edit.name,
                        "email": edit.email,
                        "password":edit.password
            }
        }
        return JsonResponse(message, status=200)  
    
class MemberDeleteAPiView(APIView):
    def delete(self,request,pk):
        print(request.data)
        edit = Member.objects.get(id=pk)
        edit.delete()
        message={ "success":"Ok"}
        return JsonResponse(message, status=200)        

