from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        #fields='__all__'
        #fields=['topic_name','name','url']
        exclude=['email']
        #help_texts={'name':'should not be integers','url':'valid url only'}
        widgets={'url':forms.PasswordInput,'name':forms.Textarea,'url':forms.CharField}
        #labels={'topic_name':'tn'}



