from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('vagas.urls')),
    path('', include('curriculo.urls')),
    path('admin/', admin.site.urls),
    path('', include('autenticacao.urls')),
    path('c/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
