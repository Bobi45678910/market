from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render

from apps.core.models import User


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(email=email).exists():
            return render(request, 'login.html', {'error': 'Пользователь не найден'})
        user = User.objects.get(email=email)
        if not user.check_password(password):
            return render(request, 'login.html', {'error': 'Неверный пароль'})
        login(request, user)
        return redirect('core:index_view')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('core:index_view')


def register_view(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        if User.objects.filter(username=data['email']).exists():
            context['error'] = 'Такой пользователь уже существует!'
        else:
            User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=make_password(data['password']),
            )
            return redirect('core:login')

    return render(request, 'register.html', context=context)
