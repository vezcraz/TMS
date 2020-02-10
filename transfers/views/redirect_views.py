from django.shortcuts import redirect

from transfers.constants import UserType

def login_redirect_view(request):
    user_type = request.user.userprofile.user_type
    if user_type == UserType.STUDENT.value:
        return redirect('/TMS/student/dashboard/')
    elif user_type == UserType.SUPERVISOR.value:
        return redirect('/TMS/hod/home/')
    elif user_type == UserType.HOD.value:
        return redirect('/TMS/supervisor/home/')
