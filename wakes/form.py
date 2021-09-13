from django import forms
from django.db import models
from django.forms import fields
from django.forms.models import ModelForm

from wakes.models import Member, Wake



class WakeForm(forms.ModelForm):
    class Meta:
        model = Wake
        fields = ('name', 'description')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Wake
        fields = ('name', 'description', 'member')
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm.self).__init__(*args, **kwargs)
        user_id = kwargs.get('instance').user.id
        self.Meta.fields['member'].queryset = Member.objects.filter(created_by=user_id)


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('name',)
