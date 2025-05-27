from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from apps.mart.forms import AdForm
from apps.mart.models.AdModel import Ad


@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.created_at = timezone.now()
            ad.updated_at = timezone.now()
            ad.save()
            return redirect('mart:create_ad')
    else:
        form = AdForm()

    return render(request, 'mart/create_ad.html', {'form': form})


def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    return render(request, 'mart/ad_detail.html', {'ad': ad})
