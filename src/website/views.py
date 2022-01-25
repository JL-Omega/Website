from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from accounts.models import MyUser
from django.urls import reverse


def authentication(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        login_email = request.POST.get('login_email')
        login_password = request.POST.get('login_password')

        if name and email and password:
            MyUser.objects.create_user(name, email, password)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect(reverse('home'))

        if login_email and login_password:
            user = authenticate(request, username=login_email, password=login_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'website/authentication.html', {'error2': 'Identifiant ou mot de passe incorrect'})
    return render(request, 'website/authentication.html')


@login_required
def home(request):
    return render(request, 'website/home.html')


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('authentication'))

