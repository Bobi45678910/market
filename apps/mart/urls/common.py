from django.urls import include, path

app_name = 'mart'

urlpatterns = [
    path('ad/', include('apps.mart.urls.ad_urls')),
    path('my_ads/', include('apps.mart.urls.ads_user_urls')),
    path('ads_by_category/', include('apps.mart.urls.ads_category_urls')),
]
