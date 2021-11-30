

import datetime
from trueHome.apps.business.models import ActivityModel


def validate_property_date_range(property, date):
    exist = False
    date = date.replace(minute=00, second=00)
    total = ActivityModel.objects.filter(
        schedule__gte=date,
        schedule__lte=date + datetime.timedelta(hours=1),
        property=property
        ).count()
    if total > 0:
        exist = True
    return exist
