from django.views import generic
from django.http import JsonResponse

from transfers.models import PS2TSTransfer, TS2PSTransfer


class AssocDeanView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        ps2ts = PS2TSTransfer.objects.all().order_by('applicant.user.username')
        ts2ps = TS2PSTransfer.objects.all().order_by('applicant.user.username')
        # fetching PS2TS data
        ps2ts_qs = PS2TSTransfer.objects.values(
            'applicant__user__username',
            'applicant__user__first_name', 'applicant__user__last_name',
            'sub_type', 'is_supervisor_approved',
            'is_hod_approved'
        )
        # fetching TS2PS data
        ts2ps_qs = TS2PSTransfer.objects.values(
            'applicant__user__username',
            'applicant__user__first_name', 'applicant__user__last_name',
            'sub_type', 'is_hod_approved'
        )
        # converting QuerySet --> List
        ps2ts_list = list(ps2ts_qs)
        ts2ps_list = list(ts2ps_qs)
        return_list = ps2ts_list + ts2ps_list        
        return JsonResponse(return_list, safe=False)
