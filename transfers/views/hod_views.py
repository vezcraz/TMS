from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from transfers.constants import UserType
from transfers.models import PS2TSTransfer, UserProfile


class HODHomeView(generic.TemplateView):
    template_name = 'transfers/common.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def get_hod_data(request):
    response = {}
    try:
        current_user = request.user
        transfer_qs = PS2TSTransfer.objects.filter(
            hod_email = current_user.email
        ).values_list(
            'applicant__user__first_name', 'cgpa', 'thesis_locale',
            'thesis_subject', 'name_of_org', 'expected_deliverables'
        )
        transfer_list = list(transfer_qs)
        response['data'] = transfer_list
        response['error'] = False
        response['message'] = 'success'
    except:
        print('Hi')
        response['data'] = []
        response['error'] = True
        response['message'] = 'error'
    return JsonResponse(response, safe=False)
