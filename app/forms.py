from django import forms
from app.models import *


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields="__all__"

class WebpageForm(forms.ModelForm):
    reemail=forms.EmailField()
    class Meta:
        model=Webpages
        fields="__all__"
        #fields=['topic_name','name']
        #exclude=['email']
        #labels={'topic_name':'TN','email':'EM'}
        #widgets={'name':forms.PasswordInput}

    def clean(self):
        em=self.cleaned_data['email']
        rem=self.cleaned_data['reemail']
        if em!=rem:
            raise forms.ValidationError('mails doesnt match')

class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields="__all__"

    