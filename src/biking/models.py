from django.db import models

from movies.models import BaseModel


class BikeRide(BaseModel):
    ride_km = models.FloatField()
    ride_avg_km = models.FloatField(null=True)
    ride_time = models.FloatField()
    ride_wind = models.FloatField()
    kcal = models.IntegerField()
    avg_heartbeat = models.IntegerField()

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.created_date, self.ride_km, self.ride_avg_km, self.ride_time, self.ride_wind, self.kcal, self.avg_heartbeat)
