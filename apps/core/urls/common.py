from django.urls import include, path

app_name = 'core'

urlpatterns = [
    path('', include('apps.core.urls.core_urls')),
    path('auth/', include('apps.core.urls.auth_urls')),
]
