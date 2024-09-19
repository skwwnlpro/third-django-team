from django.urls import path
from .views import SignUpView, EmailActivate, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("activate/<str:uidb64>/<str:token>/", EmailActivate.as_view(), name="activate_email"),
    # Simple JWT Authentication
    path("login/", LoginView.as_view()),
    path("login/refresh/", TokenRefreshView.as_view()),
]
