from django import forms
from .models import PS2TSTransfer, TS2PSTransfer

class PS2TSTransferForm(forms.ModelForm):
    class Meta:  
        model = PS2TSTransfer  
        fields = "__all__"
        labels = {
            "hod_email": "HOD Email",
            "cgpa": "CGPA",
            "name_of_org": "Name of Organization",
            "is_hod_approved": "Is HOD approved"
        }


class TS2PSTransferForm(forms.ModelForm):
    class Meta:  
        model = TS2PSTransfer  
        fields = "__all__"
        labels = {
            "hod_email": "HOD Email",
            "cgpa": "CGPA",
            "name_of_org": "Name of Organization",
            "is_hod_approved": "Is HOD approved"
        }