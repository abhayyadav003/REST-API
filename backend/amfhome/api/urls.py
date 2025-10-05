from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from api import views

urlpatterns = [
    
    # localhost:8000/api/
    path('', views.api_home),
    
    # auth tokens
    path('auth/', obtain_auth_token),
    
]

