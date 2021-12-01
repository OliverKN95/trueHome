from django_filters import rest_framework as filters
from trueHome.apps.property.models import PropertyModel


class PropertyFilter(filters.FilterSet):

    class Meta:
        model = PropertyModel
        fields = {'status', 'title'}
