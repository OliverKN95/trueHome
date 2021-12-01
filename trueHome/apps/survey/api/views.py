from rest_framework import viewsets
from django.utils.translation import ugettext as _
from trueHome.apps.survey.api.serializers import SurveySerializer
from trueHome.apps.survey.models import SurveyModel
from trueHome.apps.survey.api.filters import SurveyFilter

# from rest_framework.permissions import AllowAny


class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    queryset = SurveyModel.objects.all()
    filterset_class = SurveyFilter
    authentication_classes = []
    permission_classes = []
