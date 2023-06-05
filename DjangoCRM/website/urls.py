from django.urls import path
from . import views # we need to connect each page with a view

urlpatterns = [
    path("",views.home,name="home"),#creating homepage "" is for homepage
    # path("login/",views.login_user,name="login"),#creating homepage "" is for homepage
    path("logout/",views.logout_user,name="logout"),#creating homepage "" is for homepage
    #we have functions named login and logout...so can't name views login or logout - will conflict.
    path("register/",views.register_user,name="register"),#creating homepage "" is for homepage

]