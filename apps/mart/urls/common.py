from django.urls import include, path

app_name = 'mart'

urlpatterns = [
    path('ad/', include('apps.mart.urls.ad_urls')),
]
