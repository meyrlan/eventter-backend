import logging

from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from django.db import transaction

from core.models import (
    Profile,
    Event,
    Interest,
)

logger = logging.getLogger(__name__)


class InterestInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = ("id", "title")


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="user_id", read_only=True)
    sex = serializers.CharField(source="get_sex_display")
    interests = InterestInfoSerializer(many=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "first_name",
            "last_name",
            "sex",
            "birth_date",
            "bio",
            "interests",
        ]


class EventCreateSerializer(serializers.ModelSerializer):

    @transaction.atomic
    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Event
        fields = [
            "title",
            "capacity",
            "date",
            "time",
            "age_limit",
            "description",
            "owner",
            "interests",
        ]


class EventInfoSerializer(serializers.ModelSerializer):
    attendees = serializers.SerializerMethodField()
    remaining_capacity = serializers.SerializerMethodField()
    age_limit = serializers.IntegerField(allow_null=True)
    owner = ProfileSerializer()
    interests = InterestInfoSerializer(many=True)

    @extend_schema_field(ProfileSerializer(many=True))
    def get_attendees(self, event):
        return ProfileSerializer(event.attendees.all(), many=True, context=self.context).data

    def get_remaining_capacity(self, event) -> int:
        return max(0, event.capacity - event.attendees.count())

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "remaining_capacity",
            "date",
            "time",
            "duration",
            "photo",
            "age_limit",
            "description",
            "owner",
            "interests",
            "attendees",
        ]
