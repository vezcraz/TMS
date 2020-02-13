from constants import UserType, TransferType

from models import PS2TSTransfer, TS2PSTransfer


def application_status(userprofile):
    status = None
    alias = None
    try:
        ps2ts = PS2TSTransfer.objects.filter(applicant=userprofile)
        ts2ps = TS2PSTransfer.objects.filter(applicant=userprofile)
        if ps2ts.count() == 1:
            alias = TransferType.PS2TS.value
            status = _get_ps2ts_application_status(userprofile, ps2ts)
        elif ts2ps.count() == 1:
            alias = TransferType.TS2PS.value
            status = _get_ts2ps_application_status(userprofile. ts2ps)
        else:
            status = -1
    except Exception as e:
        status = -1
    
    return (status, alias)

def _get_ps2ts_application_status(userprofile, ps2ts):
    application = ps2ts[0]
    if not application.is_supervisor_approved and not application.is_hod_approved:
        return 0
    elif application.is_supervisor_approved and not application.is_hod_approved:
        return 1
    else:
        return 2

def _get_ts2ps_application_status(userprofile, ts2ps):
    application = ts2ps[0]
    if not application.is_hod_approved:
        return 0
    else:
        return 1
