from django.urls import path
from . import views
from .views import validate_login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import user_passes_test


app_name = "event"

unauthenticated_user = user_passes_test(lambda user: not user.is_authenticated, login_url='event:dashboard')

urlpatterns = [
    path("", unauthenticated_user(views.arrival), name="arrival"),
    path("login/", unauthenticated_user(validate_login), name="login"),
    path('register/', unauthenticated_user(views.register), name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', LogoutView.as_view(next_page='event:arrival'), name="logout"),
    path('people', views.people, name="people"),
    path('jobs', views.jobs, name="jobs"),
]