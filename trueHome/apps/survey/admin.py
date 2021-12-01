from django.contrib import admin
from trueHome.apps.survey.models import SurveyModel

# Register your models here.


@admin.register(SurveyModel)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('activity',)
    list_filter = ('activity',)
    search_fields = ['activity']
