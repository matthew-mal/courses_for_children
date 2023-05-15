from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from .forms import SignUpForm, ProfileForm
from .models import Profile


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            profile = Profile.objects.create(user=user, email=form.cleaned_data.get('email'))
            user.profile = profile  # связываем объект User с объектом Profile
            user.save()  # сохраняем объект User
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('news_home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})





@login_required
def account(request):
    profile = request.user.profile if hasattr(request.user, 'profile') else None
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'account.html', {'user_form': user_form, 'profile_form': profile_form})
