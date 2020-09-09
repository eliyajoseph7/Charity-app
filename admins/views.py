from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('admins:dashboard')
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    # else:
        # form = AuthenticationForm()    
    return render(request, 'admins/auth/login.html', {'message': _message})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('admins:login')

@login_required(login_url='/admins/login')
def home_dashboard(request):
    return render(request, 'admins/components/index.html')


@login_required(login_url='/admins/login')
def user_profile(request, id):
    profile = User.objects.get(id=id)
    return render(request, 'admins/components/profile.html', {'profile': profile})    