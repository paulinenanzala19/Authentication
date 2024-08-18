from django.contrib.auth import get_user_model
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.cache import cache
from .utils import get_user_from_cache_or_db
from django.conf import settings
import datetime


User = get_user_model()

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user_id = User.objects.get(username=serializer.data['username']).id
        user = get_user_from_cache_or_db(user_id)


        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user_id = User.objects.get(email=request.data['email']).id
            user = get_user_from_cache_or_db(user_id)

        return response

class TokenRefreshView(TokenRefreshView):
    pass

class LogoutView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            cache.delete(f'user_{request.user.id}')

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"error": "Missing 'refresh' token in request data."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)