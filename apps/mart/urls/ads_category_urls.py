from django.urls import path

from apps.mart.views.ads_category_views import ads_by_category

urlpatterns = [
    path('category/<int:category_id>/', ads_by_category, name='ads_category'),
]
