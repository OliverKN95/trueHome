from django.urls import path, include
from trueHome.apps.survey import views

app_name = 'survey'

urlpatterns = [
    # API Webservices
    path('api/', include('trueHome.apps.survey.api.urls'), name="api"),
    # Vista de encuesta
    path('survey-preview/<int:survey_id>/', views.SurveyPreviewView.as_view(), name='survey-preview'),
]
