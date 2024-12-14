from django.urls import path
from .QuanLyTaiLieuMonHoc import QuanLyTaiLieuMonHocDetail, QuanLyTaiLieuMonHocInfo
# from . import views

# urlpatterns =[
#     # path("", views.home, name="home"),
#     # path("v1/", views.v1, name="v_1")
#     path("items", views.api_items)
# ]

urlpatterns = [
    path("qltlmh/", QuanLyTaiLieuMonHocDetail.as_view(), name="qltlmh"),
    path("qltlmh/<int:id>/", QuanLyTaiLieuMonHocInfo.as_view())
]