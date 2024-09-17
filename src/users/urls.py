from django.urls import path
from .views import SignUpView, EmailActivate

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("activate/<str:uidb64>/<str:token>/", EmailActivate.as_view(), name="activate"),
]
