from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class PropertyModel(models.Model):
    """
        Modelo para almacenar las propiedades con sus datos correspondientes
    """

    STATUS_CHOICES = (
        (1, _("active")),
        (2, _("disabled")),
        (3, _("done")),
    )
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    address = models.CharField(max_length=100, verbose_name=_("Address"))
    description = models.CharField(
        max_length=100, verbose_name=_("Description"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Updated at"))
    disabled_at = models.DateTimeField(null=False,
                                       auto_now_add=True, verbose_name=_("Disabled at"))
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=1, verbose_name=_("Status"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")


class ActivityModel(models.Model):
    """
        Modelo para almacenar las actividades de las propiedades con sus datos correspondientes
    """

    STATUS_CHOICES = (
        (1, _("active")),
        (2, _("disabled")),
        (3, _("done")),
    )
    property = models.ForeignKey(
        PropertyModel, verbose_name=_("Property"), on_delete=models.CASCADE)
    schedule = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Schedule"))
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.CharField(
        max_length=100, verbose_name=_("Description"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Updated at"))
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=1, verbose_name=_("Status"))

    def __str__(self):
        return self.property.id + "-" + self.title

    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")


class SurveyModel(models.Model):
    """
        Modelo para almacenar las encuestas de las actividades con sus datos correspondientes
    """

    STATUS_CHOICES = (
        (1, _("active")),
        (2, _("disabled")),
        (3, _("done")),
    )
    activity = models.ForeignKey(
        ActivityModel, verbose_name=_("Activity"), on_delete=models.CASCADE)
    description = models.JSONField(verbose_name=_("Answers"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at"))

    def __str__(self):
        return self.activity.id + "-" + self.title

    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")
