from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('clientes/', include(clientes_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
