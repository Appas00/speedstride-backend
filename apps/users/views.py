from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer


# ✅ REGISTER USER
@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "User registered successfully"
        })

    return Response(serializer.errors, status=400)


# ✅ GET ALL USERS
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# ✅ CREATE ADMIN (FOR RENDER DEPLOY)
@api_view(['GET'])
def create_admin(request):
    if not User.objects.filter(username='appas').exists():
        User.objects.create_superuser(
            username='appas',
            email='appas@gmail.com',
            password='Appas@01'
        )
        return Response({
            "message": "Admin created successfully"
        })

    return Response({
        "message": "Admin already exists"
    })