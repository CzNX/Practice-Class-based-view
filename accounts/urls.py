from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
    # path('logout/', views.logout,name='logout'),
]
