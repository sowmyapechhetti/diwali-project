from django.urls import path
from . import views


urlpatterns = [

    path('', views.register_view, name='register'),

    path('login/', views.login_view, name='login'),

    path('diwali/', views.diwali_view, name='diwali'),

    path('logout/', views.logout_view, name='logout'),

]