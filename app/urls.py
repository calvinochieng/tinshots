from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from app.views import *

urlpatterns = [
    path('', index, name="index"),
    path('home/', home, name="home"),
    path('pricing', pricing, name = "pricing"),
    path('gallery/', gallery_view, name='gallery'),
    path('bookings/', booking_view, name='bookings'),
    path("portforlio/", portfolio, name="portforlio"), 
    path('contact/', contact_view, name='contact'),
    path("<slug:slug>/", portfolio_detail_view, name="detail"),  # General slug last
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)