from django.urls import path, include

app_name = 'property'

urlpatterns = [
    # API Webservices
    path('api/', include('trueHome.apps.property.api.urls'), name="api"),
]
