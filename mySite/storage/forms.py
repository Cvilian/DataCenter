from django import forms
 
from .models import Data
 
 
class DataForm(forms.ModelForm):
 
    class Meta:
        model = Data
        fields = ['source', 'flow_count', 'packet_count', 'size']