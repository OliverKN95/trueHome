import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from trueHome.apps.survey.models import SurveyModel
from trueHome.apps.survey.forms import SurveyForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
class SurveyPreviewView(LoginRequiredMixin, View):
    """
    Vista para la edición de parametros de la categoria
    """
    template_name = "survey_preview.html"
    form = SurveyForm

    def get(self, request, survey_id):

        survey = get_object_or_404(SurveyModel, id=survey_id)
        
        answers = []
        for key, value in survey.answers.items():
            answers.append((key, value))

        ctx = {
            'form':self.form(instance=survey),
            'survey': survey,
            'answers': answers
        }

        return render(request, self.template_name, ctx)