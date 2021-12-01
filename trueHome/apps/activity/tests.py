from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from trueHome.apps.activity.models import ActivityModel
from trueHome.apps.property.models import PropertyModel
# Create your tests here.


class AccountTests(APITestCase):

    url = reverse('activity:activity:activitymodel-list')

    def setUp(self):
        self.property = PropertyModel.objects.create(
            title="Property Yucatán 1",
            address="Calle 60 centro",
            description="Casa colonial",
            disabled_at="2021-12-03T15:32:20.792Z",
            status=1
        )
        self.activity = ActivityModel.objects.create(
            property=self.property,
            schedule="2021-01-02T11:00:00Z",
            title="testactivity",
            description="Validación de documentos de la de propiedad",
            status=1
        )
        self.activity_2 = ActivityModel.objects.create(
            property=self.property,
            schedule="2021-01-03T11:00:00Z",
            title="testactivity2",
            description="Validación de documentos de la de propiedad2",
            status=1
        )

    def test_list_activities(self):
        data = {}
        response = self.client.get(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_activity(self):
        data = {
            "schedule": "2021-01-05T11:36:00Z",
            "title": "testactivity",
            "description": "Validación de documentos de la de propiedad",
            "status": 1,
            "property": self.property.id
        }
        response = self.client.post(self.url, data, format='json')
        data_resp = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ActivityModel.objects.get(id=data_resp['id']).title, 'testactivity')

    def test_re_agend_activity(self):
        url = reverse('activity:activity:re-agend-activity')
        data = {
            "activity_id": self.activity.id,
            "schedule": "2021-01-02T11:00:00Z"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_re_agend_activity_same_date(self):
        url = reverse('activity:activity:re-agend-activity')
        data = {
            "activity_id": self.activity_2.id,
            "schedule": "2021-01-02T05:00:00Z"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cancel_activity(self):
        url = reverse('activity:activity:cancel-activity')
        data = {
            "activity_id": self.activity_2.id,
            "schedule": "2021-01-02T11:00:00Z"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        