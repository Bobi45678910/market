from django.shortcuts import get_object_or_404, render

from apps.mart.models import Ad, Category


def ads_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    subcategories = category.childrens.all()
    ids = [category.id] + [c.id for c in subcategories]

    ads = Ad.objects.filter(category__in=ids, is_active=True)
    context = {
        'category': category,
        'ads': ads,
    }
    return render(request, 'mart/ads_category.html', context=context)
