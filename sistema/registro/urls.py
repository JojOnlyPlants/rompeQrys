from django.urls import path
from .views import SignUpView, CuentaUpdate, EmailUpdate, login_view

urlpatterns = [
     path('signup/',SignUpView.as_view(),name="signup"),
     path('cuenta/',CuentaUpdate.as_view(),name="cuenta"),
     path('cuenta/email/',EmailUpdate.as_view(),name="cuenta_email"),
     path('login/', login_view, name='login'),
     path('profile/', CuentaUpdate.as_view(), name='profile'),
]
