from django.shortcuts import render
from django.views import generic

from transfers.models import PS2TSTransfer

from transfers.forms import PS2TSTransferForm, TS2PSTransferForm



class StudentDashboardView(generic.TemplateView):
    template_name = 'transfers/student_dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


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