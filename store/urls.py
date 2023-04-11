from django.urls import path
from . import views

# Create Code Here

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.Signup, name='signup')
]
