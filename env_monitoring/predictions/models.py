from django.db import models


class EnvironmentalData(models.Model):
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    sensor_data = models.JSONField()  # Stores environmental sensor data

    def __str__(self):
        return f"{self.location} at {self.timestamp}"
