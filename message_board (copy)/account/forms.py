from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
# from django.http import HttpResponse
# from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    
    class Meta:
        model = User
        fields = ["username","password1", "password2","dob"]
        widgets={'dob':forms.DateInput(attrs={'class':'dob'})}
        labels={'dob':'Date of Birth'}
        
        def clean_dob(self):
            dob=self.cleaned_data.get('dob')
            
            if dob!='j':
                raise forms.ValidationError('what')
            return dob


