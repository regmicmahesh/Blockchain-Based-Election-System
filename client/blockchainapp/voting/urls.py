from django.urls import path
from .views import DashboardView, ResultView

app_name = "voting"

urlpatterns = [
    path("running", DashboardView.as_view(), name="running"),
    path("result", ResultView.as_view(), name="result")
]