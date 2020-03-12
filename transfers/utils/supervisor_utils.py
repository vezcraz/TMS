# Supervisor user utility functions
from django.core.mail import send_mail
from .constants import UserType, TransferType, ThesisLocaleType, ApplicationsStatus
from django.http import JsonResponse
from .models import PS2TSTransfer, TS2PSTransfer, DeadlineModel
from django.utils import timezone as datetime
