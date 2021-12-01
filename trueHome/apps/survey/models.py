from django.db import models
from django.utils.translation import ugettext_lazy as _
from trueHome.apps.activity.models import ActivityModel

# Create your models here.


class SurveyModel(models.Model):
    """
        Modelo para almacenar las encuestas de las actividades con sus datos correspondientes
    """

    activity = models.OneToOneField(
        ActivityModel, verbose_name=_("Activity"), on_delete=models.CASCADE)
    description = models.JSONField(verbose_name=_("Answers"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at"))

    def __str__(self):
        return str(self.activity.id) + "-" + self.activity.title

    class Meta:
        verbose_name = _("Survey")
        verbose_name_plural = _("Surveys")
