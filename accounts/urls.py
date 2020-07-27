from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration_view, name='registration_view'),
    path('login/', views.login_view, name='login_view'),



]