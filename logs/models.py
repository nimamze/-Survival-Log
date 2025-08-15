from django.db import models
from survivors.models import Survivor


class Zone(models.Model):
    name = models.CharField(max_length=10)
    is_safe = models.BooleanField()


class Log(models.Model):
    survivor = models.ForeignKey(
        Survivor, on_delete=models.CASCADE, related_name="survivor_log"
    )
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="zone_log")
    note = models.TextField()
    zombie_amount = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)


class ZoneConnection(models.Model):
    date = models.DateField(auto_now_add=True)
    note = models.TextField()
    seen_zombie = models.BooleanField()
    survivor = models.ForeignKey(
        Survivor, on_delete=models.CASCADE, related_name="survivor_zone_connection"
    )
    from_zone = models.OneToOneField(
        Zone, on_delete=models.CASCADE, related_name="from_zone_zone_connection"
    )
    to_zone = models.OneToOneField(
        Zone, on_delete=models.CASCADE, related_name="to_zone_zone_connection"
    )
