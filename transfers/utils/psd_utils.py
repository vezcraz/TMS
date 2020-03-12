# This file will contain utility functinos related to psd user
from django.core.mail import send_mail
from transfers.constants import UserType, TransferType, ThesisLocaleType, ApplicationsStatus
from django.http import JsonResponse
from transfers.models import PS2TSTransfer, TS2PSTransfer, DeadlineModel
from django.utils import timezone as datetime


def update_psd_data(form):
    try:
        update_psd = DeadlineModel.objects.all().first()
    except:
        update_psd = DeadlineModel.objects.create()
    update_psd.deadline_PS2TS = form.cleaned_data.get('deadline_PS2TS')
    update_psd.deadline_TS2PS = form.cleaned_data.get('deadline_TS2PS')
    update_psd.message = form.cleaned_data.get('message')
    update_psd.is_active_PS2TS = form.cleaned_data.get('is_active_PS2TS')
    update_psd.is_active_TS2PS = form.cleaned_data.get('is_active_TS2PS')
    update_psd.save()
