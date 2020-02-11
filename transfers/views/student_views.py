from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse

from transfers.constants import CampusType, UserType
from transfers.models import PS2TSTransfer, UserProfile
from transfers.forms import PS2TSTransferForm, TS2PSTransferForm


class StudentDashboardView(generic.TemplateView):
    template_name = 'transfers/student_dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class PS2TSFormView(generic.FormView):
    form_class = PS2TSTransferForm
    initial = {'key': 'value'}
    template_name = 'transfers/PS2TS.html'
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        # is supervisor email valid (present in DB)?
        invalid_supervisor_email = False
        form.fields["applicant"].queryset = UserProfile.objects.filter(user_type=0)
        hod_email_qs = UserProfile.objects.filter(
            user_type=UserType.HOD.value
            ).values_list(
                'user__email', flat=True
                )
        hod_email_list = list(hod_email_qs)
        self.context = {
            'form': form,
            'hod_email_list': hod_email_list,
            'invalid_supervisor_email': invalid_supervisor_email
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # is supervisor email valid (present in DB)?
        invalid_supervisor_email = False
        if form.is_valid():
            email = form.cleaned_data.get('supervisor_email')
            supervisor_email_qs = UserProfile.objects.filter(
                user_type=UserType.SUPERVISOR.value, user__email__contains=email)
            if supervisor_email_qs:
                form.save()
                return render(request, "transfers/student_dashboard.html")
            else:
                invalid_supervisor_email = True
        form.fields["applicant"].queryset = UserProfile.objects.filter(user_type=UserType.STUDENT.value)
        hod_email_qs = UserProfile.objects.filter(
            user_type=UserType.HOD.value
            ).values_list(
                'user__email', flat=True
                )
        hod_email_list = list(hod_email_qs)
        self.context = {
            'form': form,
            'hod_email_list': hod_email_list,
            'invalid_supervisor_email': invalid_supervisor_email
        }
        return render(request, self.template_name, self.context)
        

class TS2PSFormView(generic.FormView):
    form_class = TS2PSTransferForm
    initial = {'key': 'value'}
    template_name = 'transfers/TS2PS.html'
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        form.fields["applicant"].queryset = UserProfile.objects.filter(user_type=0)
        hod_email_qs = UserProfile.objects.filter(
            user_type=UserType.HOD.value
            ).values_list(
                'user__email', flat=True
                )
        hod_email_list = list(hod_email_qs)
        self.context = {'form': form, 'hod_email_list': hod_email_list}
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "transfers/student_dashboard.html")
        form.fields["applicant"].queryset = UserProfile.objects.filter(user_type=0)
        hod_email_qs = UserProfile.objects.filter(
            user_type=UserType.HOD.value
            ).values_list(
                'user__email', flat=True
                )
        hod_email_list = list(hod_email_qs)
        self.context = {'form': form, 'hod_email_list': hod_email_list}
        return render(request, self.template_name, self.context)

def validate_supervisor_email(request):
    email = request.GET.get('email', None)
    supervisor_email_list = UserProfile.objects.filter(
        user_type=UserType.SUPERVISOR.value, user__email__contains=email
    )
    is_valid = False
    if supervisor_email_list:
        is_valid = True
        name = supervisor_email_list[0].user.get_full_name()
        campus = supervisor_email_list[0].campus
        if campus == CampusType.GOA.value:
            campus = "BITS Pilani, Goa Campus"
        elif campus == CampusType.HYD.value:
            campus = "BITS Pilani, Hyderabad Campus"
        elif campus == CampusType.Pilani.value:
            campus = "BITS Pilani, Pilani Campus"
    data = {
        'is_valid': is_valid,
        'name': name,
        'campus': campus
    }
    return JsonResponse(data)
