from django.urls import path
from . import views
from .views import validate_login


app_name = "event"

urlpatterns = [
    path("", views.arrival, name="arrival"),
    path("login/", validate_login, name="login"),

]