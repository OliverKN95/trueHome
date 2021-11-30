import json
import datetime
from django.db import transaction
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.utils.translation import ugettext as _
from trueHome.apps.business.api.serializers import PropertySerializer, ActivitySerializer, SurveySerializer, ReAgendActivitySerializer
from trueHome.apps.business.models import PropertyModel, ActivityModel, SurveyModel
from trueHome.apps.business.api.filters import PropertyFilter, ActivityFilter, SurveyFilter
from trueHome.apps.global_functions import validate_property_date_range
from django.shortcuts import get_object_or_404

# from rest_framework.permissions import AllowAny


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

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            # Se valida que la propiedad no este deshabilitada
            if data['property'].status == 2:
                message = _(
                    "La propiedad seleccionada no admite actividades ya que se encuentra deshabilitada.")
                return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)
            exist = validate_property_date_range(
                data['property'], data['schedule'])
            if exist:
                message = _(
                    "La fecha y hora seleccionada ya que se encuentra en uso por otra actividad.")
                return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)
            # Generamos nuevo registro
            with transaction.atomic():
                new_activity = ActivityModel.objects.create(
                    property=data['property'],
                    schedule=data['schedule'].replace(minute=00, second=00),
                    title=data['title'],
                    description=data['description'],
                    # updated_at=serializer.validated_data['updated_at'],
                    status=data['status']
                )
                new_activity.updated_at = new_activity.created_at
                new_activity.save()
                serializer = ActivitySerializer(
                    new_activity, context={'request': request})
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReAgendActivityView(GenericAPIView):
    serializer_class = ReAgendActivitySerializer
    queryset = ActivityModel.objects.all().exclude(status=4)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            activity = get_object_or_404(self.queryset, pk=data['activity_id'])
            # Validamos que la actividad no se encuentre deshabilitada
            if activity.status == 4:
                message = _(
                    "La actividad seleccionada no puede ser re agendada debido a que se encuentra cancelada.")
                return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)
            # Validamos que no se empalmen las fechas y horas
            exist = validate_property_date_range(
                activity.property, data['schedule'])
            if exist:
                message = _(
                    "La fecha y hora seleccionada ya que se encuentra en uso por otra actividad.")
                return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)
            # Generamos nuevo registro
            with transaction.atomic():
                activity.schedule = data['schedule'].replace(minute=00, second=00)
                activity.save()
                serializer = ActivitySerializer(
                    activity, context={'request': request})
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    queryset = SurveyModel.objects.all()
    filterset_class = SurveyFilter
    authentication_classes = []
    permission_classes = []
