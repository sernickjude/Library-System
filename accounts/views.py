from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('photo_album:album_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        print(f"DEBUG: username={username}, password={password}, confirm={confirm_password}")

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, password=password)
            auth_login(request, user)
            print("DEBUG: User created and logged in successfully")
            return redirect('photo_album:album_list')

    return render(request, 'accounts/registration.html')