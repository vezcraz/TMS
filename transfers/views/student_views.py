from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views import View, generic
from django.contrib import messages

from transfers.models import PS2TSTransfer

from transfers.forms import PS2TSTransferForm, TS2PSTransferForm



class StudentDashboardView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        full_name = current_user.get_full_name()
        current_user_profile = current_user.userprofile
        approved_applications = PS2TSTransfer.objects.filter(
            applicant=current_user_profile, is_supervisor_approved=True)
        pending_applications = PS2TSTransfer.objects.filter(
            applicant=current_user_profile, is_supervisor_approved=False)

        if approved_applications.count() == 0:
            messages.info(request, 'You have no approved applications')
        if pending_applications .count() == 0:
            messages.info(request, 'You have no pending applications')

        return render(request, 'transfers/student_landing.html', {
            'full_name': full_name,
            'approved_applications': approved_applications,
            'pending_applications': pending_applications})

    def post(self, request, *args, **kwargs):
        if 'ts2ps' in request.POST:
            print("thesis to practice school")
        elif 'ps2ts' in request.POST:
            print("practice school to thesis")

        # will raise error because of missing return statement


class PS2TSFormView(generic.FormView):
    form_class = PS2TSTransferForm
    initial = {'key': 'value'}
    template_name = 'transfers/PS2TS.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

class TS2PSFormView(generic.FormView):
    form_class = TS2PSTransferForm
    initial = {'key': 'value'}
    template_name = 'transfers/TS2PS.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
