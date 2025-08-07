from rest_framework import serializers
from .models import Zone, Log, ZoneConnection


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        exclude = ["date"]

    def create(self, validated_data):
        log = Log.objects.create(
            note=validated_data["note"],
            zombie_amount=validated_data["zombie_amount"],
            zone=validated_data["zone"],
            survivor=validated_data["survivor"],
        )
        return log


class ZoneConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneConnection
        exclude = ["date"]

    def create(self, validated_data):
        zoneConnection = ZoneConnection.objects.create(
            note=validated_data["note"],
            seen_zombie=validated_data["seen_zombie"],
            from_zone=validated_data["from_zone"],
            to_zone=validated_data["to_zone"],
            survivor=validated_data["survivor"],
        )
        return zoneConnection


class LogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"


class LogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        exclude = ["date"]


class ZoneConnectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneConnection
        fields = "__all__"
