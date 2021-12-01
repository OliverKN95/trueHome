from django.db import models
from django.utils.translation import ugettext_lazy as _
from trueHome.apps.property.models import PropertyModel

# Create your models here.


class ActivityModel(models.Model):
    """
        Modelo para almacenar las actividades de las propiedades con sus datos correspondientes
    """

    STATUS_CHOICES = (
        (1, _("active")),
        (2, _("disabled")),
        (3, _("done")),
        (4, _("canceled")),
    )
    property = models.ForeignKey(
        PropertyModel, verbose_name=_("Property"), on_delete=models.CASCADE)
    schedule = models.DateTimeField(
        auto_now_add=False, verbose_name=_("Schedule"))
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.CharField(
        max_length=100, verbose_name=_("Description"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated at"))
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=1, verbose_name=_("Status"))

    def __str__(self):
        return str(self.property.id) + "-" + self.title

    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")
