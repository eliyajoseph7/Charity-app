from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def unauthenticated_user(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('admins:dashboard')
            else:    
                return view_func(request, *args, **kwargs)

        return wrapper_func    


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:    
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return wrapper_func
    return decorator                