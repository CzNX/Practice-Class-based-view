from django.contrib import admin
from django.urls import path
from. import views
from .views import index,detail,create,update,delete


urlpatterns = [
    path('', index.as_view(),name='index'),
    path('create/', create.as_view(),name='create'),
    path('<int:pk>/update/', update.as_view(),name='update'),
    path('<int:pk>/', detail.as_view(),name='detail'),
    path('<int:pk>/delete', delete.as_view(),name='delete'),
    path('search/',views.search ,name='search'),
]
