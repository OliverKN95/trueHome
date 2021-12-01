from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from trueHome.apps.survey.models import SurveyModel


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyModel
        fields = "__all__"
