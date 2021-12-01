from django.utils.translation import ugettext as _
from django import forms
from trueHome.apps.survey.models import SurveyModel


class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyModel
        fields = '__all__'
