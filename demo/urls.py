from django.contrib import admin
from django.urls import path
from django.views import debug

from .views import error, index

admin.autodiscover()

urlpatterns = [
    path("", debug.default_urlconf),
    path("admin/", admin.site.urls),
    path("demo/", index),
    path("demo/error/", error, name="force_error"),
]
