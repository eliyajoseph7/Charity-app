from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from hope.models import Contact, Portfolio
from django.http import HttpResponse
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.hashers import make_password
import json

# Create your views here.
@unauthenticated_user
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

@login_required(login_url='/admins/login')
def update_profile(request, id):
    if request.method == 'POST':
        _fname = request.POST['first_name']
        _lname = request.POST['last_name']
        _username = request.POST['username']
        _email = request.POST['email']

        profile = User.objects.get(id=id)
        profile.first_name = _fname
        profile.last_name = _lname
        profile.username = _username
        profile.email = _email
        profile.save()

        profile.profile.gender = request.POST['gender']
        profile.profile.save()
        return redirect('admins:user_profile', id)    


@login_required(login_url='admins/login')
@allowed_users(allowed_roles=['admin'])
def users_view(request):
    users = User.objects.all().order_by('id')
    context = {'users':users}
    return render(request, 'admins/components/user_management.html', context)        


@login_required(login_url='admins/login')
def inbox_view(request):
    contacts = Contact.objects.all().order_by('date')
    count = Contact.objects.all().count()

    return render(request, 'admins/components/inbox.html', {"contacts": contacts, "count": count})   


@login_required(login_url='admins/login')
def email_view(request, slug):
    info = Contact.objects.get(slug=slug)

    return render(request, 'admins/components/read_email.html', {'info': info})     

def update_staff(request, id):
     if request.method == 'POST':
        user = User.objects.get(id=id) 
        _fname = request.POST['fname']
        _lname = request.POST['lname']
        _username = request.POST['username']
        _email = request.POST['email']

        user.first_name = _fname
        user.last_name = _lname
        user.username = _username
        user.email = _email
        user.save()

        user.profile.gender = request.POST['gender']
        user.profile.save()
        return redirect('admins:users')   


@login_required(login_url='admins/login')
def portfolio_view(request):
    portfolios = Portfolio.objects.all().order_by('-id')
    return render(request, 'admins/components/portfolios.html', {'portfolios': portfolios})       


def update_portfolio(request, slug):
    if request.method == 'POST':
        portfolio = Portfolio.objects.get(slug=slug)  

        title = request.POST['title']
        description = request.POST['description']
        category    = request.POST['category']
        image       = request.POST['img_url']

        portfolio.title = title
        portfolio.description = description   
        portfolio.category = category   
        portfolio.img_url = image 
        portfolio.save()

        return redirect('admins:portfolio')  


def create_portfolio(request):
    if request.method == 'POST':
        title       = request.POST['title']
        category    = request.POST['category']
        description = request.POST['description']
        img_url     = request.POST['img_url']

        portfolio   = Portfolio(title=title, category=category, description=description, img_url=img_url)
        portfolio.save()
        return HttpResponse('portfolio created successfully')


def delete_portfolio(request, slug):
    if request.method == 'POST':
        Portfolio.objects.get(slug=slug).delete()

        return redirect('admins:portfolio')


# Update password 
def update_password(request, id):
    user = User.objects.get(id=id)
    usr = User.objects.filter(id=id)
    if request.method == 'POST':
        current = request.POST['currentPass']
        newPassword = request.POST['password']
        newPasswordConf = request.POST['passwordConf']

        check = user.check_password(current)

        if(check is False):
            return HttpResponse(json.dumps({'mismatch': 'current password is incorrect'}),
                        content_type="application/json"
                        )
        else:
            if(len(newPassword) < 8):
                    return HttpResponse(json.dumps({'passError': 'password should contain atleast 8 characters'}),
                            content_type="application/json"
                            )
            else:
                if(newPassword != newPasswordConf):
                    return HttpResponse(json.dumps({'confError': 'passwords do not match'}),
                                content_type="application/json"
                                )
                
                else:
                    password=make_password(newPassword,hasher='default')
                    usr.update(password=password)    
                    return HttpResponse(json.dumps({'success': 'passwords updated successfully'}),
                                content_type="application/json"
                                )    