# accounts/urls.py
from django.urls import path
from .views import CustomLoginView
from .views import CustomSignupView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    
]