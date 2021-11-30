from django.contrib import admin
from trueHome.apps.business.models import ActivityModel, PropertyModel, SurveyModel

# Register your models here.
@admin.register(PropertyModel)
class PropertyAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ['title']
    
    
@admin.register(ActivityModel)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ['title']
    
    
@admin.register(SurveyModel)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('activity',)
    list_filter = ('activity',)
    search_fields = ['activity']