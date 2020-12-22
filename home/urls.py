from django.urls import path
from .views import home, system_logout

urlpatterns = [
    path('', home, name="home"),
    path("logout/", system_logout, name = "logout"),
]