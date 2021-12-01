from django.urls import path
from trueHome.apps.activity.api.views import ActivityViewSet, ReAgendActivityView, CancelActivityView
from rest_framework import routers

app_name = 'activity'

router = routers.SimpleRouter()
router.register(r'activity', ActivityViewSet)

urlpatterns = [
    path('re_agend_activity/', ReAgendActivityView.as_view(), name='re-agend-activity'),
    path('cancel_activity/', CancelActivityView.as_view(), name='cancel-activity'),
]

urlpatterns = router.urls + urlpatterns

