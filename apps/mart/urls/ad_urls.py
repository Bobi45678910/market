from django.urls import path

from apps.mart.views.ad_views import ad_detail, create_ad

urlpatterns = [
    path('create/', create_ad, name='create_ad'),
    path('<int:pk>/', ad_detail, name='ad_detail'),
]
