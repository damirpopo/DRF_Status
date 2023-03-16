from django.shortcuts import render
from .models import Order,TitleJob,Status,Workers
from .serializers import Orderserializer,TitleJobserializer,Statusserializer,Workersserializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def order_list(request):
    if request.method == "GET":
        order = Order.objects.all()
        serializer = Orderserializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = Orderserializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def TitleJob_detail(request,pk):
    try:
        titleJob=TitleJob.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = TitleJobserializer(titleJob)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = TitleJobserializer(titleJob,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        titleJob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def titleJob_list(request):
    if request.method == "GET":
        order = TitleJob.objects.all()
        serializer = TitleJobserializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = TitleJobserializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def Workers_detail(request,pk):
    try:
        order=Workers.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = Workersserializer(order)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = Workersserializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def Workers_list(request):
    if request.method == "GET":
        order = Workers.objects.all()
        serializer = Workersserializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = Workersserializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def Status_detail(request,pk):
    try:
        order=Status.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = Statusserializer(order)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = Statusserializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def Status_list(request):
    if request.method == "GET":
        order = Status.objects.all()
        serializer = Statusserializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = Statusserializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def order_detail(request,pk):
    try:
        order=Order.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = Orderserializer(order)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = Orderserializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

