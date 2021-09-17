from django import forms
from django.db import models
from django.forms import fields
from django.forms.models import ModelForm

from wakes.models import Member, Wake



class WakeForm(forms.ModelForm):
    class Meta:
        model = Wake
        fields = ('name', 'description')


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('name',)


class SelectMemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_id = kwargs.get('instance').created_by.id
        self.fields['member'].widget = forms.CheckboxSelectMultiple()
        self.fields['member'].queryset = Member.objects.filter(created_by=user_id)
        



    class Meta:
        model = Wake
        fields = ('member',)
