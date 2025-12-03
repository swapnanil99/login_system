from django.urls import path
from .views import *

urlpatterns = [
    path("", login_view, name="login_page"),   
    path("dashboard/", dashboard_view, name="dashboard"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
]
