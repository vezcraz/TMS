from django.shortcuts import redirect

from transfers.constants import UserType


def login_redirect_view(request):
    current_user_type = request.user.userprofile.user_type
    if (current_user_type == UserType.STUDENT.value):
        return redirect('student_dashboard')
    else:
        # for temporary purpose
        return redirect('student_dashboard')
