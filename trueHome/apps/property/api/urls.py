from django.urls import path
from trueHome.apps.property.api.views import PropertyViewSet
from rest_framework import routers

app_name = 'property'

router = routers.SimpleRouter()
router.register(r'property', PropertyViewSet)

urlpatterns = [
]

urlpatterns = router.urls + urlpatterns
