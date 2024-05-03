from django.urls import path
from .views import CuentaListView, CuentaDetailView

urlpatterns = [
    path('', CuentaListView.as_view(), name='lista'),
    path('<username>/', CuentaDetailView.as_view(), name='detalles'),
]
