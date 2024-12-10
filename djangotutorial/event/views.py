from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.

def arrival(request):
    return render(request, 'event/arrival.html')

def signin(request):
    return render(request, 'event/login.html')

def validate_login(request):
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['first_name'] = user.first_name
                return redirect('event:dashboard')
            else:
                error_message = "Invalid Credentials"
        else:
            error_message = " Please correct the errors below."
    else:
        form = LoginForm()

    return render(request, "event/login.html", {'form': form, 'error_message': error_message})