from django.urls import path, include

from member import views

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path("user/find-id/", views.find_id, name="find_id"),
    path("user/change-pw/", views.ChangePasswordView.as_view(), name="change_pw"),

]
