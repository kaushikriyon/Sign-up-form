from django.urls import path

from . import views

urlpatterns = [
    path('', views.Login,name="login"),
    path('signup', views.Signup,name="signup"),
    path('getlogindata', views.get_login_data,name="getlogindata"),
    path('getsignupdata', views.get_signup_data,name="getsignupdata"),
]