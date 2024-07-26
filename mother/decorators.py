from django.http import HttpResponse
from django.shortcuts import redirect, render


def allowed_users(allowed_roles= []):
    def decorator(view_func):
        def wrapper_func(request,*arg,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(group)
            if group in allowed_roles:
                return view_func(request,*arg,**kwargs)
            else:
                return redirect('main')
        return wrapper_func
    return decorator