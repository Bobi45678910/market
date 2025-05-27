from django.shortcuts import render

from apps.mart.models import Category


def index_view(request):
    main_categories = Category.objects.filter(parent__isnull=True)

    context = {
        'main_categories': main_categories
    }
    return render(request, 'index.html', context=context)


def about_view(request):
    return render(request, 'about.html')
