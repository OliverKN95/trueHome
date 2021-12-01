from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from trueHome.apps.property.models import PropertyModel


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyModel
        fields = "__all__"
