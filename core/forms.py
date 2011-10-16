__author__ = 'kir'
from django import forms

class FeedbackForm(forms.Form):
    subject=forms.CharField()
    message=forms.CharField()
    sender=forms.EmailField()