from django.shortcuts import render
from django.views import generic


class SupervisorHomeView(generic.TemplateView):
    template_name = 'transfers/common.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
