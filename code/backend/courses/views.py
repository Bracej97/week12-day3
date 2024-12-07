from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer, LoginSerializer, RegisterSerializer
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView


from drf_yasg.utils import swagger_auto_schema



@swagger_auto_schema(method='post',request_body=LoginSerializer)
@api_view(['POST'])
def loginpost(request):
    serializer = LoginSerializer(data = request.data)
    if not serializer.is_valid():
        return Response({
            "status": False,
            "data": serializer.errors
        })
    username = serializer.data['username']
    password = serializer.data['password']

    user = User.objects.filter(username=username).first()
    user_obj = authenticate(username=username, password=password)
    user_data = {
        "id": user.id,
        "name": f"{user.first_name} {user.last_name}".strip() if user.first_name or user.last_name else user.username,
        "token": str(Token.objects.get_or_create(user=user_obj)[0].key),
    }
    if user_obj:
        return Response({
            "status": True,
            "data": user_data
        })

    return Response({
        "status": True,
        "data": {},
        "message": "Invalid Credentials"
    })

class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            user_data = {
                "id": user.id,
                "username": user.username,
                "email" : getattr(user, "email", "")
            }
            return Response({
                "status": True,
                "message": "User Created Successfully",
                "data" : user_data
            }, status= status.HTTP_201_CREATED)
        return Response({
            "status": False,
            "message": serializer.errors
        }, status= status.HTTP_400_BAD_REQUEST)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None):
        course = self.get_object()
        course.users.add(request.user)
        course.save()
        return Response({'status': 'enrolled successfully'})

    @action(detail=True, methods=['post'])
    def unenroll(self, request, pk=None):
        course = self.get_object()
        course.users.remove(request.user)
        course.save()
        return Response({'status': 'unenrolled successfully'})
