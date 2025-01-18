from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('', include('app.urls')),
    path('terms', terms, name = 'terms')
]