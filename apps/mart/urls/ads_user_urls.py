from django.urls import path

from apps.mart.views.ads_user_views import user_ads

urlpatterns = [
    path('', user_ads, name='ads_user'),    
]
