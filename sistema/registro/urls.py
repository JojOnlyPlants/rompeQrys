from django.urls import path
from .views import SignUpView, CuentaUpdate, EmailUpdate

urlpatterns = [
     path('signup/',SignUpView.as_view(),name="signup"),
     path('cuenta/',CuentaUpdate.as_view(),name="cuenta"),
     path('cuenta/email/',EmailUpdate.as_view(),name="cuenta_email"),
]
