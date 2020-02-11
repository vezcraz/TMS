from django import forms
from .models import PS2TSTransfer, TS2PSTransfer, UserProfile

class PS2TSTransferForm(forms.ModelForm):
    class Meta:  
        model = PS2TSTransfer  
        fields = ['applicant', 'supervisor_email', 'hod_email', 'sub_type', 'cgpa', 'thesis_locale', 'thesis_subject', 'name_of_org', 'expected_deliverables']
        labels = {
            "hod_email": "HOD Email",
            "cgpa": "CGPA",
            "name_of_org": "Name of Organization"
        }


class TS2PSTransferForm(forms.ModelForm):
    class Meta:  
        model = TS2PSTransfer  
        fields = ['applicant', 'hod_email', 'sub_type', 'cgpa', 'reason_for_transfer', 'name_of_org']
        labels = {
            "hod_email": "HOD Email",
            "cgpa": "CGPA",
            "name_of_org": "Name of Organization"
        }