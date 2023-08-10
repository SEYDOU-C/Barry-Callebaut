from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from authenticate.views import CallebautLogin, CallebautLogout

urlpatterns = [
    path('',CallebautLogin, name="login"),
    path('logout/',CallebautLogout, name="logout"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
