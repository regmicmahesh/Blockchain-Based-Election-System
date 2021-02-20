from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import User
from django.shortcuts import redirect
# Create your views here.


class LoginView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "login.html")
    
    def post(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect("/")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == None or password == None:
            messages.error("Username or Password is not provided.")
        
        user = authenticate(request,username=username,password=password)
        if not user:
            messages.error("Username or password is invalid.")
            return render(request, "login.html")
        else:
            login(request,user=user)
            return redirect("/")

class SignupView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "signup.html")

    def post(self, request: HttpRequest):
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            phone = request.POST.get("phone")
            citizenship_number = request.POST.get("citizenship_number")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password)
            #TODO: VAlidate everything.



def logoutView(request):
    logout(request)
    return redirect("/auth/")