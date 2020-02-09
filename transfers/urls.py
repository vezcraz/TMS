from django.urls import path

from transfers.views import redirect_views, student_views


urlpatterns = [
    path('login-redirect/', redirect_views.login_redirect_view),
    path('PS2TS/', student_views.PS2TSFormView.as_view()),
    path('TS2PS/', student_views.TS2PSFormView.as_view()),
    path('student-dashboard/', student_views.StudentDashboardView.as_view()),
]
