from django.contrib import admin
from trueHome.apps.activity.models import ActivityModel

# Register your models here.


@admin.register(ActivityModel)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ['title']
