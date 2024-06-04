from django.contrib import admin
from django.urls import path, include
from pages.views import feed  # Asegúrate de importar la vista 'feed'
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns

from django.conf import settings
urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include('pages.urls')),
    path('feed/', feed, name='feed'),  # Aquí definimos la ruta 'feed/'

    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),
    # Paths de Messenger
    path('messenger/', include(messenger_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)