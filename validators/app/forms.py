from app.models import *
from django import forms
from django.core.validators import (MinLengthValidator,MaxLengthValidator,RegexValidator,EmailValidator,URLValidator)

def check_len(value):
    if len(value)>10:
        raise forms.ValidationError('length is greater than 10')
     
def check_k(value):
    if value.lower()[0]=='k':
        raise forms.ValidationError('name starts with k')

class Topicform(forms.Form):
    topic_name=forms.CharField(validators=[check_len,check_k])


class TopicModelform(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class Webpageform(forms.ModelForm):
    name = forms.CharField(validators=[MaxLengthValidator(10)])
    reemail=forms.EmailField()
    bot=forms.CharField(widget=forms.HiddenInput,required=False)
    class Meta:
        model=Webpage
        fields='__all__'

    # def clean_topic_name(self):
    #     obj=self.cleaned_data.get('name')
    #     if obj and len(obj)>10:
    #         raise forms.ValidationError("too long")
    #     return obj
    
    def clean_bot(self):
        bott=self.cleaned_data['bot']
        if len(bott)>0:
            raise forms.ValidationError('bot has catched')

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reemail']
        if e and re and e != re:
            raise forms.ValidationError('emails are not matched')

        return self.cleaned_data
