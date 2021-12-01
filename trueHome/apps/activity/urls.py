from django.urls import path, include

app_name = 'activity'

urlpatterns = [
    # API Webservices
    path('api/', include('trueHome.apps.activity.api.urls'), name="api"),
]
