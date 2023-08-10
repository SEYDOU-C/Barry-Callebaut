from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from blog.views import CallebautAcceuil

urlpatterns = [
    path('',CallebautAcceuil, name="Acceuil"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
