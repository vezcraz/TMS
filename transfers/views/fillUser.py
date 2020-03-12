from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.shortcuts import redirect
from django.http import HttpResponse

from transfers.constants import CampusType, UserType, TransferType
from transfers.models import PS2TSTransfer, UserProfile
from transfers.forms import PS2TSTransferForm, TS2PSTransferForm

from transfers.tools.populate import populate


def fill(request):
	if request.method=='GET':
		return render(request, 'transfers/fill.html')
	if request.method=='POST':
		if request.user.is_superuser:
			populate(request)
	return HttpResponse("Done")
