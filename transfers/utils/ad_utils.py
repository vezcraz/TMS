# File that has all the utility functions for pages related to assoc-dean
from django.core.mail import send_mail
from transfers.constants import UserType, TransferType, ThesisLocaleType, ApplicationsStatus
from django.http import JsonResponse
from transfers.models import PS2TSTransfer, TS2PSTransfer, DeadlineModel
from django.utils import timezone as datetime


def fetch_ps2ts_list():
    ps2ts = PS2TSTransfer.objects.all().order_by('applicant.user.username')
    # fetching PS2TS data
    ps2ts_qs = PS2TSTransfer.objects.values(
        'applicant__user__username',
        'applicant__user__first_name', 'applicant__user__last_name',
        'sub_type', 'is_supervisor_approved',
        'is_hod_approved', 'cgpa', 'thesis_locale', 'supervisor_email',
            'thesis_subject', 'name_of_org', 'expected_deliverables'
    )
    # converting QuerySet --> List
    ps2ts_list = list(ps2ts_qs)
    return ps2ts_list

def fetch_ts2ps_list():
    ts2ps = TS2PSTransfer.objects.all().order_by('applicant.user.username')
    # fetching TS2PS data
    ts2ps_qs = TS2PSTransfer.objects.values(
        'applicant__user__username',
        'applicant__user__first_name', 'applicant__user__last_name',
        'sub_type', 'is_hod_approved', 'cgpa', 
            'reason_for_transfer', 'name_of_org', 
    )
    # converting QuerySet --> List
    ts2ps_list = list(ts2ps_qs)
    return ts2ps_list
