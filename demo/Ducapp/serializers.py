from rest_framework import serializers
from Ducapp.models import QuanLyTaiLieuHocTap

class qltlhtSerializer(serializers.ModelSerializer):
    class Meta:
        model =  QuanLyTaiLieuHocTap
        fields = ["idLopHoc","idTaiLieu","tenTaiLieu","description","loaiTaiLieu","link"]