from django.urls import path

from core.views import Homepage, info


urlpatterns = [
    path('', Homepage.as_view(), name = 'homepage'),
    path('info/', info.as_view(), name = 'info'),
]