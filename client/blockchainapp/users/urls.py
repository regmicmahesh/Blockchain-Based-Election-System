from django.urls import path
from .views import LoginView, logoutView, SignupView

app_name = "auth"

urlpatterns = [
    path("", LoginView.as_view(), name='login'),
    path("signup", SignupView.as_view(), name='signup'),

    path("logout", logoutView, name="logout")
]