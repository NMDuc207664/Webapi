# from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import api_view
# from .serializers import qltlhtSerializer
# from .models import QuanLyTaiLieuHocTap
# from rest_framework.response import Response
# #Create your views here.
# # def home(request):
# #     return HttpResponse("Hello world")
# # def v1(request):
# #     return HttpResponse("<h1>v1</h1>")
# @api_view()
# def api_items(request):
#     items = QuanLyTaiLieuHocTap.objects.all()
#     serializer = qltlhtSerializer(items, many=True)
#     return Response(serializer.data)

# @api_view()
# def api_item(request, pk):
#     item = get_object_or_404(QuanLyTaiLieuHocTap, id=pk)
#     serializer = qltlhtSerializer(item)
#     return Response(serializer.data)