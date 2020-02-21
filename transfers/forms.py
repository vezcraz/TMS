from django import forms
from .models import PS2TSTransfer, TS2PSTransfer, UserProfile, DeadlineModel

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

class PSDForm(forms.ModelForm):
    class Meta:
        model = DeadlineModel
        fields = ['deadline_PS2TS', 'is_active_PS2TS','deadline_TS2PS', 'is_active_TS2PS', 'message']
        labels = {
            'deadline_PS2TS' : 'Deadline Date and Time',
            'is_active_PS2TS' : 'Enable/Disable',
            'deadline_TS2PS' : 'Deadline Date and Time',
            'is_active_TS2PS' : 'Enable/Disable',
            'message': 'Message to be Displayed'
        }
