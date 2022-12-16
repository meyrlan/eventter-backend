from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.v2.client.views import (
    ProfileAPIView,
    EventAPIView,
    ListAllEventsAPIView,
    EventCreateAPIView,
)

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path("profile/<int:pk>", ProfileAPIView.as_view(), name="profile"),
    path("event/<int:pk>", EventAPIView.as_view(), name="event"),
    path("event/create", EventCreateAPIView.as_view(), name="event"),
    path("events/all", ListAllEventsAPIView.as_view(), name="events"),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
