from django.urls import path, include

app_name = 'survey'

urlpatterns = [
    # API Webservices
    path('api/', include('trueHome.apps.survey.api.urls'), name="api"),
]
