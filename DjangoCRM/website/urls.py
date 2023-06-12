from django.urls import path
from . import views # we need to connect each page with a view (. means everything)

urlpatterns = [
    path("",views.home,name="home"),#creating homepage "" is for homepage
    # path("login/",views.login_user,name="login"),#creating homepage "" is for homepage
    path("logout/",views.logout_user,name="logout"),#creating homepage "" is for homepage
    #we have functions named login and logout...so can't name views login or logout - will conflict.
    path("register/",views.register_user,name="register"),#creating homepage "" is for homepage
    path("record/<int:pk>",views.customer_record,name="record"),#<integer as primary key>
    path("delete_record/<int:pk>",views.delete_record,name="delete_record"),#need to pass primary key to know which record to delete
    path("add_record/",views.add_record,name="add_record"),#creating homepage "" is for homepage
    path("update_record/<int:pk>",views.update_record,name="update_record"),#creating homepage "" is for homepage
    path("profile_list/",views.profile_list,name="profile_list"),
    path("view_records/",views.view_records,name="view_records"),
    path("profile/<int:pk>",views.profile,name="profile"),

]