from django.urls import path
from trueHome.apps.business.api.views import PropertyViewSet, ActivityViewSet, SurveyViewSet, ReAgendActivityView
from rest_framework import routers

app_name = 'business'

router = routers.SimpleRouter()
router.register(r'property', PropertyViewSet)
router.register(r'activity', ActivityViewSet)
router.register(r'survey', SurveyViewSet)

urlpatterns = [
    path('re_agend_activity/', ReAgendActivityView.as_view()),
]

urlpatterns = router.urls + urlpatterns

