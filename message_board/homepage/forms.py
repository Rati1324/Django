from django import forms
from .import models

class CreatePost(forms.ModelForm):
    
    class Meta:
        model=models.Post
        fields=['title','body']
        
        widgets = {
          'body': forms.Textarea(attrs={'style':'resize:vertical;max-height:500px;width:405px'}),
        }
    
        
        
class Comment_form(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''
    
    class Meta:
        model=models.Comment
        fields=['body']
        
        widgets={
            'body':forms.Textarea(attrs={'style':'resize:none;background-color:Transparent;border-radius:10px;\
                                          border:none;width:631px;height:180px;margin-top:2px',})
            }
          
    