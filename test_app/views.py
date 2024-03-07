# views.py
from django.http import JsonResponse
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from .models import bme280
from .serializers import YourModelSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import Group, User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestView(APIView):
    def get(self, request):
        queryset = bme280.objects.all()
        serializer = YourModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def return_raw_json(request):
    queryset = User.objects.all().order_by('-date_joined')
    data = list(queryset.values())  # Convert queryset to list of dictionaries
    return JsonResponse(data, safe=False)


def return_raw_json_sensor(request):
    queryset = bme280.objects.all()
    data = list(queryset.values())  # Convert queryset to list of dictionaries

    return JsonResponse(data, safe=False)
