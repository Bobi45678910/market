from django.urls import path

from apps.core.views.edit_profile_views import edit_profile

urlpatterns = [
    path('profile/edit/', edit_profile, name='edit_profile'),
]
