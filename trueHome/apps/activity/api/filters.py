from django_filters import rest_framework as filters
from trueHome.apps.activity.models import ActivityModel


class ActivityFilter(filters.FilterSet):

    class Meta:
        model = ActivityModel
        fields = {'status', 'title'}
