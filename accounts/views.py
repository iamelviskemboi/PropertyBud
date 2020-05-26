from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import (redirect, render)

from .forms import (UserRegistrationForm)


# Accounts/ -> REGISTER
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password2']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)


# Accounts -> SETTINGS
@login_required
def settings(request):
    return render(request, 'accounts/settings.html')


# Accounts/ -> LOGIN
def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Username or password is incorrect!')
    else:
        return redirect('home')
    return render(request, 'accounts/login.html')


# Accounts/ -> LOGOUT
@login_required
def sign_out(request):
    logout(request)
    return redirect('login')
