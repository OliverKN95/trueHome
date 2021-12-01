from django.contrib import admin
from trueHome.apps.property.models import PropertyModel

# Register your models here.


@admin.register(PropertyModel)
class PropertyAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)

    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ['title']
