from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Election
from datetime import datetime
# Create your views here.
class DashboardView(LoginRequiredMixin, UserPassesTestMixin, View):
    
    login_url = '/auth/'

    def test_func(self):
        return self.request.user.isvoter 

    def get(self, request):

        current_date = datetime.date(datetime.now())
        context = {}
        registered_elections = Election.objects.filter(voter__user__username=request.user.username).filter(expiry_date__gt=current_date);
        context["elections"] = registered_elections;
        context["username"] = request.user.username;
        
        return render(request, "vote.html", context);
    
    def post(self, request):

        voted_id = request.POST.get("votedId")
        print(voted_id)

class ResultView(LoginRequiredMixin, UserPassesTestMixin, View):
    
    login_url = '/auth/'

    def test_func(self):
        return self.request.user.isvoter 

    def get(self, request):

        current_date = datetime.date(datetime.now())
        context = {}
        registered_elections = Election.objects.filter(voter__user__username=request.user.username).filter(expiry_date__lt=current_date);
        context["elections"] = registered_elections;
        context["username"] = request.user.username;
        
        return render(request, "results.html", context);
    
 