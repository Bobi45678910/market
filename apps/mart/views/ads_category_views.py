from django.shortcuts import get_object_or_404, render

from apps.mart.models import Ad, Category


def ads_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    subcategories = category.childrens.all()

    if subcategories.exists():
        context = {
            'category': category,
            'subcategories': subcategories,
        }
        return render(request, 'mart/subcategories.html', context)

    ads = Ad.objects.filter(category=category, is_active=True)
    context = {
        'category': category,
        'ads': ads,
    }
    return render(request, 'mart/ads_category.html', context)
