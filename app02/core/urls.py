from django.urls import path
from .views import HomePageView, SamplePageView, PageCreate  # Asegúrate de importar PageCreate

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('page_create/', PageCreate.as_view(), name='page_create'),  # Aquí es donde defines la ruta para PageCreate
]