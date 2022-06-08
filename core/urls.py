from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simple_pages.urls')),


    # car_wash - все пути для мойки
    path('car_wash/', include('car_wash.urls')),
    path('auto_parts/', include('auto_parts.urls')),
    path('tire_fitting/', include('tire_fitting.urls')),


    path('accounts/', include('django.contrib.auth.urls')), # all
    path('accounts/', include('accounts.urls')), #register

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)