from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import User, Voter
from django.shortcuts import redirect
from django.conf import settings
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

def handle_uploaded_file(f):
    filename = f'{settings.BASE_DIR / "media" / "profile_pictures"}/{f.name}'
    # fp = open(filename, "w");
    # fp.close()
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class SignupView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "signup.html")

    def post(self, request: HttpRequest):
            print(request.POST)
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            phone = request.POST.get("phone")
            citizenship_number = request.POST.get("citizenship_number")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
              # print(request.FILES)
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password)
            user.citizenship_number = citizenship_number
          
            image = request.FILES['image']
            handle_uploaded_file(image)
            user.image = "profile_pictures/" + image.name
            user.save()

            voter = Voter.objects.create(user=user)
            voter.save()
            return redirect("/")
            



def logoutView(request):
    logout(request)
    return redirect("/auth/")