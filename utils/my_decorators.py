# ye model dige ke beshe etelaat am ferestad be decorator to video khodesh yad mide
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse


def permission_checker_decorator(func):
    def wrapper(request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('login_page'))

    return wrapper
