from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from api.v2.client.serializers import ProfileSerializer, EventInfoSerializer, EventCreateSerializer
from core.models import Profile, Event


# --- Views ---


class ProfileAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = None
    permission_classes = [AllowAny]


class EventAPIView(RetrieveAPIView):
    http_method_names = ["get"]
    queryset = Event.objects.all()
    serializer_class = EventInfoSerializer
    pagination_class = None
    permission_classes = [AllowAny]


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventCreateSerializer
    permission_classes = [AllowAny]


class ListAllEventsAPIView(ListAPIView):
    http_method_names = ["get"]
    queryset = Event.objects.all()
    serializer_class = EventInfoSerializer
    pagination_class = None
    permission_classes = [AllowAny]
