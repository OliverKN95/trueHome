from django_filters import rest_framework as filters
from trueHome.apps.survey.models import SurveyModel


class SurveyFilter(filters.FilterSet):

    class Meta:
        model = SurveyModel
        fields = {'activity__title', }
