from rest_framework import viewsets
from django.utils.translation import ugettext as _
from trueHome.apps.property.api.serializers import PropertySerializer
from trueHome.apps.property.models import PropertyModel
from trueHome.apps.property.api.filters import PropertyFilter

# from rest_framework.permissions import AllowAny


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = PropertyModel.objects.all()
    filterset_class = PropertyFilter
    authentication_classes = []
    permission_classes = []
