from django_filters import rest_framework as filters
from trueHome.apps.business.models import PropertyModel, ActivityModel, SurveyModel


class PropertyFilter(filters.FilterSet):

    class Meta:
        model = PropertyModel
        fields = {'status', 'title'}


class ActivityFilter(filters.FilterSet):

    class Meta:
        model = ActivityModel
        fields = {'status', 'title'}


class SurveyFilter(filters.FilterSet):

    class Meta:
        model = SurveyModel
        fields = {'activity__title', }


# class RedeemCouponFilter(filters.FilterSet):

#     class Meta:
#         model = RedeemCoupon
#         fields = {'user', 'coupon', 'reward', 'redeem_status', 'confirmed_redeem_by', 'coupon__company',
#                   'reward__company'}
