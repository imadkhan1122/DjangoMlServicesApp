from django.urls import include, re_path
from django.contrib import admin
# from django.urls import path

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    re_path('admin/', admin.site.urls),
]

urlpatterns += endpoints_urlpatterns