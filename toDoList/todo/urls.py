from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('', views.auth, name='auth'),
    path('about/', views.about, name='about'),
]