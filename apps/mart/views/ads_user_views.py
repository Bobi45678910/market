from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.mart.models.AdModel import Ad


@login_required
def user_ads(request):
    ads = Ad.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'mart/ads_user.html', {'ads': ads})
