from django.db import models
import traceback
import random, string

# Create your models here.
class QuanLyTaiLieuHocTap(models.Model):
    idLopHoc = models.IntegerField(db_column='IDLopHoc')
    idTaiLieu = models.IntegerField(db_column='IDTaiLieu', primary_key=True)
    tenTaiLieu = models.CharField(db_column='TenTaiLieu', max_length=200)
    description = models.CharField(db_column='Descriptions', max_length=800, null=True)
    loaiTaiLieu = models.CharField(db_column='LoaiTaiLieu', max_length=100)
    link = models.CharField(db_column='Link', max_length=255)
    def __str__(self):
        return self.name

