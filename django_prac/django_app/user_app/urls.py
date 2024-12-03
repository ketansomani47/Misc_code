from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import register, logout

from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView
urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),

    path('api/token/', TokenObtainPairView.as_view(), name='get-token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]
