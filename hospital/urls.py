
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.homepage),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('saveform', views.saveform, name="saveform"),
]
