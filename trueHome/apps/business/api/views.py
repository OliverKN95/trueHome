import json
import datetime
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.utils.translation import ugettext as _
from trueHome.apps.business.api.serializers import PropertySerializer, ActivitySerializer, SurveySerializer
from trueHome.apps.business.models import PropertyModel, ActivityModel, SurveyModel
from trueHome.apps.business.api.filters import PropertyFilter, ActivityFilter, SurveyFilter
# from rest_framework.permissions import AllowAny


# class SumaApiView(GenericAPIView):
#     serializer_class = SumaSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             data_json = {
#                 "result": serializer.validated_data["valor_a"] + serializer.validated_data["valor_b"],
#             }
#             return Response(data=data_json, status=status.HTTP_200_OK)
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = PropertyModel.objects.all()
    filterset_class = PropertyFilter
    authentication_classes = []
    permission_classes = []


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = ActivityModel.objects.all()
    filterset_class = ActivityFilter
    authentication_classes = []
    permission_classes = []


class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    queryset = SurveyModel.objects.all()
    filterset_class = SurveyFilter
    authentication_classes = []
    permission_classes = []