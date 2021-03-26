from django.forms import ModelForm
from .models import Feedback
from django import forms


class FeedbackForm(ModelForm):

    class Meta:

        model = Feedback
        fields = '__all__'
        widgets = {

            'competency': forms.RadioSelect(
                attrs={'class': 'fieldclass'}),
            'teachings_Skills': forms.RadioSelect(
                attrs={'class': 'fieldclass'}),
            'punctuality': forms.RadioSelect(
                attrs={'class': 'fieldclass'}),
            'practical_Knowlegde': forms.RadioSelect(
                attrs={'class': 'fieldclass'}),
            'approachability': forms.RadioSelect(
                attrs={'class': 'fieldclass'}),
            'class_Control': forms.RadioSelect(
                attrs={'class': 'fieldclass'}),

        }
