from django.urls import path, include

app_name = 'business'

urlpatterns = [
    # API Webservices
    path('api/', include('trueHome.apps.business.api.urls'), name="api"),
]
