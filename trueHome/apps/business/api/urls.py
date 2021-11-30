from django.urls import path
from trueHome.apps.business.api.views import PropertyViewSet, ActivityViewSet, SurveyViewSet
from rest_framework import routers

app_name = 'business'

router = routers.SimpleRouter()
router.register(r'property', PropertyViewSet)
router.register(r'activity', ActivityViewSet)
router.register(r'survey', SurveyViewSet)

urlpatterns = [
    # path('sum-nums/', SumaApiView.as_view()),
]

urlpatterns = router.urls + urlpatterns

