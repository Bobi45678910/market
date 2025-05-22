from django.urls import path

from apps.mart.views.ad_views import create_ad

urlpatterns = [
    path('create/', create_ad, name='create_ad'),
]
