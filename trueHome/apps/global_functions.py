

import datetime
from trueHome.apps.business.models import ActivityModel, SurveyModel


def validate_property_date_range(property, date):
    exist = False
    date = date.replace(minute=00, second=00)
    total = ActivityModel.objects.filter(
        schedule__gte=date,
        schedule__lte=date + datetime.timedelta(hours=1),
        property=property
    ).exclude(status=4).count()
    if total > 0:
        exist = True
    return exist


def validate_condition(activity):
    condition = ""
    date = datetime.datetime.now().replace(hour=0, minute=0, second=0)
    
    if activity.status == 1 and activity.schedule >= date:
        condition = "Pendiente a realizar"
    elif activity.status == 1 and activity.schedule < date:
        condition = "Atrasada"
    elif activity.status == 3:
        condition = "Finalizada"
    elif activity.status == 2:
        condition = "Deshabilidata"
    elif activity.status == 2:
        condition = "Cancelada"
    else:
        condition = "Ninguna"
    return condition


def get_survey_by_activity_id(activity_id):
    try:
        survey = SurveyModel.objects.get(activity=activity_id)
    except Exception as e:
        survey = None
    return survey


