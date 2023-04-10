from django.urls import path
from . import views

# Create Code Here

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.Signup)
]
