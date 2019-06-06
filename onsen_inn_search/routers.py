from django.urls import include, path
from rest_framework import routers
from onsen_inns.views import OnsenViewSet, OnsenInnViewSet

router = routers.DefaultRouter()

router.register(r'onsens', OnsenViewSet)
router.register(r'onsen_inns', OnsenInnViewSet)
