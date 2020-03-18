# Student user utility functions
from django.core.mail import send_mail
from transfers.constants import UserType, TransferType, ThesisLocaleType, ApplicationsStatus
from django.http import JsonResponse
from transfers.models import PS2TSTransfer, TS2PSTransfer, DeadlineModel
from django.utils import timezone as datetime

def get_application_status(userprofile):
    status = None
    alias = None
    has_applied = None
    error = None
    try:
        ps2ts = PS2TSTransfer.objects.filter(applicant=userprofile)
        ts2ps = TS2PSTransfer.objects.filter(applicant=userprofile)
        if ps2ts.count() == 1:
            alias = TransferType.PS2TS.value
            has_applied = 1
            error = 0
            status = _get_ps2ts_application_status(userprofile, ps2ts)
        elif ts2ps.count() == 1:
            alias = TransferType.TS2PS.value
            has_applied = 1
            status = _get_ts2ps_application_status(userprofile, ts2ps)
            error = 0
        else:
            status = -1
            has_applied = 0
            error = 0
    except Exception as e:
        status = -1
        has_applied = 0
        error = 1
    
    return (alias, has_applied, status, error)

def _get_ps2ts_application_status(userprofile, ps2ts):
    application = ps2ts[0]
    # until both supervisor and hod approves the application, the status remains 0
    if application.is_supervisor_approved == ApplicationsStatus.REJECTED.value or \
        application.is_hod_approved == ApplicationsStatus.REJECTED.value:
        return ApplicationsStatus.REJECTED.value
    else:
        return application.is_hod_approved * application.is_supervisor_approved

def _get_ts2ps_application_status(userprofile, ts2ps):
    application = ts2ps[0]
    return application.is_hod_approved

def get_branch_from_branch_code(branch_code):
    switcher = {
        'A1': 'B.E. Chemical Engineering',
        'A3': 'B.E. Electrical and Electronics Engineering',
        'A4': 'B.E. Mechanical Engineering',
        'A7': 'B.E. Computer Science Engineering',
        'A8': 'B.E. Electronics and Instrumentation Engineering',
        'AA': 'B.E. Electronics and Communication Engineering',
        'B1': 'M.Sc. Biology + ',
        'B2': 'M.Sc. Chemistry + ',
        'B3': 'M.Sc. Economics + ',
        'B4': 'M.Sc. Mathematics + ',
        'B5': 'M.Sc. Physics + ',
        'PS': ''
    }
    return switcher.get(branch_code, "Invalid branch code")
def notify_ps2ts(request):
    body = ""
    data=PS2TSTransfer.objects.filter(applicant = request.user.userprofile)[0]
    print(str(data.hod_email))
    body =  str("\nID: " + data.applicant.user.username+
    "\nName: " + data.applicant.user.first_name + " " +data.applicant.user.last_name +
    "\nTransfer Type: " + data.get_sub_type_display()+
    "\nCGPA: " + str(data.cgpa)+
    "\nThesis Locale: " + data.get_thesis_locale_display()+
    "\nThesis Subject: " + data.thesis_subject+
    "\nOrganization Name: " + data.name_of_org+
    "\nExpected Outcome: " + data.expected_deliverables)
    mail(data,request,body)

def notify_ts2ps(request):
    body = ""
    data=TS2PSTransfer.objects.filter(applicant = request.user.userprofile)[0]
    body =  str("\nID: " + data.applicant.user.username+
    "\nName: " + data.applicant.user.first_name + " " +data.applicant.user.last_name +
    "\nTransfer Type: " + data.get_sub_type_display()+
    "\nCGPA: " + str(data.cgpa)+
    "\nReason For Transfer: " + data.reason_for_transfer+
    "\nOrganization Name: " + data.name_of_org)
    mail(data,request,body)

def mail(data, request, body):
    send_mail("Transfer Application: " + request.user.username, body,
        'psdmail2020@gmail.com',[str(data.hod_email)],
        fail_silently=False)

def get_authority_comments(userprofile):
    ps2ts = PS2TSTransfer.objects.filter(applicant=userprofile)
    ts2ps = TS2PSTransfer.objects.filter(applicant=userprofile)
    comments_from_ad = ""
    comments_from_supervisor = ""
    comments_from_hod = ""
    if ps2ts.count() == 1:
        comments_from_hod = ps2ts[0].comments_from_hod
        comments_from_supervisor = ps2ts[0].comments_from_supervisor
        comments_from_ad = ps2ts[0].comments_from_ad
    elif ts2ps.count() == 1:
        comments_from_hod = ts2ps[0].comments_from_hod
        comments_from_ad = ts2ps[0].comments_from_ad
    return (comments_from_hod, comments_from_supervisor, comments_from_ad)