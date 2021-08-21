from django import forms
from django.db import models
from django.forms import fields
from django.forms.models import ModelForm

from wakes.models import Wake

class WakeForm(forms.ModelForm):
    class Meta:
        model = Wake
        fields = ('name', 'description')