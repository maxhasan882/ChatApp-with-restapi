
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from . import views
from .serializers import CustomJWTSerializer

urlpatterns = [
    path('registration/', views.UserCreate.as_view(), name='registration'),
    path('token/', views.TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='my_token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
