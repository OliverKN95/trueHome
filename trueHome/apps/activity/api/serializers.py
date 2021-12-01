from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from trueHome.apps.activity.models import ActivityModel
from trueHome.apps.property.api.serializers import PropertySerializer
from trueHome.apps.survey.api.serializers import SurveySerializer
from trueHome.apps.global_functions import validate_condition, get_survey_by_activity_id


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityModel
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super(ActivitySerializer, self).to_representation(instance)
        condition = validate_condition(instance)
        survey = get_survey_by_activity_id(instance.id)
        representation['property'] = PropertySerializer(instance.property).data
        representation['condition'] = condition
        representation['survey'] = SurveySerializer(survey, context=self.context).data
        return representation


class ReAgendActivitySerializer(serializers.Serializer):
    """
    Serializer para reagendar actividad
    """
    activity_id = serializers.IntegerField()
    schedule = serializers.DateTimeField()

class CancelActivitySerializer(serializers.Serializer):
    """
    Serializer para cancelar actividad
    """
    activity_id = serializers.IntegerField()
