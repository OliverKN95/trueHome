from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from trueHome.apps.business.models import ActivityModel, PropertyModel, SurveyModel

# class CompanySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Company
#         fields = "__all__"

#     def to_representation(self, instance):
#         representation = super(CompanySerializer, self).to_representation(instance)
#         representation['owner'] = UserSerializer(instance.owner).data

#         return representation


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyModel
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityModel
        fields = "__all__"


class ReAgendActivitySerializer(serializers.Serializer):
    """
    Serializer para reagendar actividad
    """
    activity_id = serializers.IntegerField()
    schedule = serializers.DateTimeField()


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyModel
        fields = "__all__"
