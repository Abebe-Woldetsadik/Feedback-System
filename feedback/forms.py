from django import forms
from . models import Feedback, Teacher


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['teacher', 'content']

        widgets = {
            'teacher': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-control shadow-sm', 'rows': 8, 'style': 'resize:none,'}),
        }
