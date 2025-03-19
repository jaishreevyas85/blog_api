from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from .tasks import send_welcome_email

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    send_welcome_email.delay(user.email)  # Async call
    return user
