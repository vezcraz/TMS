from django.http import HttpResponseRedirect

from functools import wraps

from transfers.constants import UserType


def getUser(request):
    return request.user.userprofile.user_type

def redirect():
    return HttpResponseRedirect('transfers/login-redirect')

def student_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        profile_type = getUser(request)
        if profile_type == UserType.STUDENT.value:
            return function(request, *args, **kwargs)
        else:
            return redirect()
    return wrap

def supervisor_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        profile_type = getUser(request)
        if profile_type == UserType.SUPERVISOR.value:
            return function(request, *args, **kwargs)
        else:
            return redirect()
    return wrap

def hod_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        profile_type = getUser(request)
        if profile_type == UserType.HOD.value:
            return function(request, *args, **kwargs)
        else:
            return redirect()
    return wrap

def ad_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        profile_type = getUser(request)
        if profile_type == UserType.AD.value:
            return function(request, *args, **kwargs)
        else:
            return redirect()
    return wrap

def psd_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        profile_type = getUser(request)
        if profile_type == UserType.PSD.value:
            return function(request, *args, **kwargs)
        else:
            return redirect()
    return wrap
