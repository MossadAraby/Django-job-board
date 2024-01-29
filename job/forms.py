from django import forms
from .models import Jobs, apply_job

class ApplyJob(forms.ModelForm):
    class Meta:
        model = apply_job
        fields = ('name', 'email','portfolio_url','cv','cover_letter')
        
        
class AddJob(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
        exclude =  ('owner','slug',)