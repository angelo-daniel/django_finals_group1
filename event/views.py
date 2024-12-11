from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def arrival(request):
    if request.user.is_authenticated:
        return redirect('event:dashboard')

    return render(request, 'event/arrival.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('event:dashboard')

    return render(request, 'event/login.html')

def validate_login(request):
    if request.user.is_authenticated:
        return redirect('event:dashboard')

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

def register(request):

    if request.user.is_authenticated:
        return redirect('event:dashboard')

    error_message = None

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            # messages.success(request, "Your account has been created!")
            request.session['first_name'] = user.first_name
            return redirect('event:login')
        else:
            error_message = "Please correct the errors below."
    else:
        form = CustomUserCreationForm()

    return render(request, 'event/register.html', {'form': form, 'error_message': error_message})

@login_required
def dashboard(request):
    response = render(request, 'event/dashboard.html')

    response['Cache-Control'] = 'no-store'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response

def logout_view(request):
    logout(request)
    request.session.clear()

    response = redirect('event/arrival.html')
    response['Cache-Control'] = 'no-store'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response

@login_required
def people(request):
    response = render(request, 'event/people.html')

    response['Cache-Control'] = 'no-store'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response

@login_required
def jobs(request):
    response = render(request, 'event/jobs.html')

    response['Cache-Control'] = 'no-store'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response