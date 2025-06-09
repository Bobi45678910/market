from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.core.forms import CustomPasswordChangeForm, CustomUserChangeForm


@login_required
def edit_profile(request):
    user_form = CustomUserChangeForm(instance=request.user)
    password_form = CustomPasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            user_form = CustomUserChangeForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect('edit_profile')

        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)
                return redirect('edit_profile')

    context = {
        'user_form': user_form,
        'password_form': password_form,
    }
    return render(request, 'core/edit_profile.html', context)
