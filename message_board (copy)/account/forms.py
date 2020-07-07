from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
# from django.http import HttpResponse
# from django.contrib.auth.models import User
from datetime import date,datetime

def age(dob):
    dob=' '.join(dob.split('-'))
    dob=datetime.strptime(dob,'%Y %M %d')
    
    today = date.today() 
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) 
  
    return age 

class RegisterForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    def clean_dob(self):
        dob=self.cleaned_data.get('dob')
            
        if age(dob)<18:
            raise forms.ValidationError('You must be 18 or older to join')
        return dob
        
    class Meta:
        model = User
        fields = ["username","password1", "password2","dob"]
        widgets={'dob':forms.DateInput(attrs={'class':'dob','type':'date'})}
        labels={'dob':'Date of Birth'}
        
        


