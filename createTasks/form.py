from django import forms
from django.forms.widgets import Textarea

class NameForm(forms.Form):
    nomDeTache = forms.CharField(widget=Textarea,label='tache: ', max_length=255, )