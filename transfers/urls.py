from django.urls import path
from django.conf.urls import url

from transfers.views import (redirect_views, student_views,
    hod_views, supervisor_views, assoc_dean_views)


# view related urls
urlpatterns = [
    # student urls
    path('login-redirect/', redirect_views.login_redirect_view),
    path('student/PS2TS/', student_views.PS2TSFormView.as_view()),
    path('student/TS2PS/', student_views.TS2PSFormView.as_view()),
    path('student/dashboard/', student_views.StudentDashboardView.as_view()),
    path('validate_supervisor_email/', student_views.validate_supervisor_email),
    # hod urls
    path('hod/home/', hod_views.HODHomeView.as_view()),
    path('hod/get-hod-data/', hod_views.get_hod_data),
    path('hod/approve-transfer-request/', hod_views.approve_transfer_request),
    # supervisor urls
    path('supervisor/home/', supervisor_views.SupervisorHomeView.as_view()),
    path('supervisor/get-supervisor-data/', supervisor_views.get_supervisor_data),
    path('supervisor/approve-transfer-request/', supervisor_views.approve_transfer_request),
    # AD urls
    path('assoc_dean/home/', assoc_dean_views.AssocDeanView.as_view()),
    path('assoc-dean/home/type/<type>', assoc_dean_views.AssocDeanView.as_view()),
]

# data related urls
urlpatterns += [
    path('data/get-application-data/', redirect_views.application_data_redirect_view),
    path('data/approve-transfer-request/', redirect_views.approve_transfer_request_redirect_view),
]