from django.urls import path
from trueHome.apps.survey.api.views import SurveyViewSet
from rest_framework import routers

app_name = 'survey'

router = routers.SimpleRouter()
router.register(r'survey', SurveyViewSet)

urlpatterns = [
]

urlpatterns = router.urls + urlpatterns
