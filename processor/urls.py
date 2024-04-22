
from django.contrib import admin
from django.urls import path, include
from processor.views import Index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="Home"),
    path('aqib-plaltes/',include('core_account.urls')),
    path('aqib-plaltes/',include('core_control.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
