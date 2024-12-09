from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignupSerializer, SigninSerializer, CategorySerializer, AssetSerializer
from .models import *

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
import jwt
from datetime import datetime, timedelta
from django.conf import settings

@api_view(['POST'])
def signup(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists'}, status=400)
    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'Email already exists'}, status=400)
    user = User.objects.create_user(username=username, email=email, password=password)
    return JsonResponse({'message': 'User registered successfully'}, status=201)

@api_view(['POST'])
def signin(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        payload = {
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=24),
            'iat': datetime.utcnow(),
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return JsonResponse({'token': token}, status=200)
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import JWTAuthentication
from .models import Asset, Category
from .serializers import AssetSerializer, CategorySerializer

@api_view(['GET', 'POST'])
def asset_list_create(request):
    if request.method == 'GET':
        assets = Asset.objects.filter(user=request.user)
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def asset_update_delete(request, id):
    try:
        asset = Asset.objects.get(id=id, user=request.user)
    except Asset.DoesNotExist:
        return Response({'error': 'Asset not found'}, status=404)

    if request.method == 'PUT':
        serializer = AssetSerializer(asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        asset.delete()
        return Response({'message': 'Asset deleted successfully'}, status=204)

@api_view(['GET', 'POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
