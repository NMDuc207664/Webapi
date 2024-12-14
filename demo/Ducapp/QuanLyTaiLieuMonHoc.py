from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from .serializers import qltlhtSerializer
from .models import QuanLyTaiLieuHocTap
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import traceback
import random, string
import datetime
from rest_framework_simplejwt.tokens import RefreshToken

#####################################################################
User = get_user_model()

# Create your views here.
def is_valid_param(param) :
    return param != " " and param is not None and param != ""


def id_generator (size, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class QuanLyTaiLieuMonHocDetail(APIView):
    def get(self, request):
        # headers = { 
        #     "Authorization": f"Bearer {access_token}", 
        #     "Content-Type": "application/json", 
        # }
        obj = QuanLyTaiLieuHocTap.objects.all()
        serializer = qltlhtSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # headers = { 
        #     "Authorization": f"Bearer {access_token}", 
        #     "Content-Type": "application/json", 
        # }
        while True:
            idTaiLieu = id_generator(size=5)
            if (QuanLyTaiLieuHocTap.objects.filter(idTaiLieu = idTaiLieu).count() == 0):
                break
        data=request.data
        data["idTaiLieu"] = idTaiLieu
        serializer = qltlhtSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "message": "Mon Hoc successfully created"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()    
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class QuanLyTaiLieuMonHocInfo(APIView):
    def get(self, request, id):
        # headers = { 
        #     "Authorization": f"Bearer {access_token}", 
        #     "Content-Type": "application/json", 
        # }
        try:
            obj=QuanLyTaiLieuHocTap.objects.get(idTaiLieu=id)
        except QuanLyTaiLieuHocTap.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = qltlhtSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            # headers = { 
            #     "Authorization": f"Bearer {access_token}", 
            #     "Content-Type": "application/json", 
            # }
            obj=QuanLyTaiLieuHocTap.objects.get(idTaiLieu=id)
        except QuanLyTaiLieuHocTap.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = qltlhtSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            # headers = { 
            #     "Authorization": f"Bearer {access_token}", 
            #     "Content-Type": "application/json", 
            # }
            obj=QuanLyTaiLieuHocTap.objects.get(idTaiLieu=id)
            obj.delete()
        except QuanLyTaiLieuHocTap.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        return Response({"msg":"deleted"}, status=status.HTTP_204_NO_CONTENT)