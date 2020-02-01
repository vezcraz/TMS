from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .constants import CampusType, TransferType, UserType


class UserProfile(models.Model):
    user_choices = [
        (UserType.STUDENT.value, 'Student'),
        (UserType.AD.value, 'Associate Dean'),
        (UserType.HOD.value, 'Head of Department'),
        (UserType.PSD.value, 'PS-Division'),
    ]
    campus_choices = [
        (CampusType.GOA.value, 'Goa'),
        (CampusType.HYD.value, 'Hyderabad'),
        (CampusType.PILANI.value, 'Pilani'),
    ]

    user = models.OneToOneField(User, primary_key=True,
        on_delete=models.CASCADE)
    campus = models.IntegerField(choices=campus_choices, blank=True,
        null=True)
    contact = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(choices=user_choices, blank=True,
        null=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile()
        user_profile.user = instance
        user_profile.save()
    instance.userprofile.save()


class Application(models.Model):
    transfer_choices = [
        (TransferType.PS2TS.value, 'PS to TS'),
        (TransferType.TS2PS.value, 'TS to PS'),
    ]

    applicant = models.OneToOneField(UserProfile, primary_key=True,
        on_delete=models.CASCADE)
    cgpa = models.DecimalField(max_digits=6, decimal_places=2)
    transfer_type = models.IntegerField(choices=transfer_choices)


class PS2TSTransfer(models.Model):
    PS2TS = 0
    OTHER = 1
    sub_type_choices = [
        (PS2TS, 'PS to TS (Single Degree)'),
        (OTHER, 'PS-TS/TS-PS to TS-TS (Dual Degree)'),
    ]

    ON_CAMPUS = 0
    OFF_CAMPUS_INDIA = 1
    OFF_CAMPUS_ABROAD = 2
    thesis_locale_choices = [
        (ON_CAMPUS, 'On Campus'),
        (OFF_CAMPUS_INDIA, 'Off Campus (India)'),
        (OFF_CAMPUS_ABROAD, 'Off Campus Abroad'),
    ]

    application = models.OneToOneField(Application, primary_key=True,
        on_delete=models.CASCADE)
    thesis_locale = models.IntegerField(choices=thesis_locale_choices)
    thesis_subject = models.CharField(max_length=150,
        help_text='Broad area/Title of Thesis')
    name_of_org = models.CharField(max_length=100,
        help_text='Name of BITS Campus or Organization where thesis will be carried')
    supervisor_name = models.CharField(max_length=100)
    supervisor_email = models.EmailField()
    expected_deliverables = models.TextField(help_text='Expected outcome of thesis')
    hod_email = models.EmailField()


class TS2PSTransfer(models.Model):
   TS2PS = 0
   PSTS2PSPS = 1
   TSTS2TSPS = 2
   sub_type_choices = [
    (TS2PS, 'TS to PS (Single Degree)'),
    (PSTS2PSPS, 'PS-TS to PS-PS (Dual Degree)'),
    (TSTS2TSPS, 'TS-TS to TS-PS (Dual Degree)'),
    ]

   application = models.OneToOneField(Application, primary_key=True,
        on_delete=models.CASCADE)
   sub_type = models.IntegerField(choices=sub_type_choices)
   reson_for_transfer = models.TextField()
   name_of_org = models.CharField(max_length=100,
        help_text='Name of BITS Campus or Organization where thesis was being carried')
   hod_email = models.EmailField()
