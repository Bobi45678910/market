from django.urls import path

from apps.core.views.core_views import about_view, index_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('about/', about_view, name='about_view'),
]
