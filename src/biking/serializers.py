from rest_framework import serializers

from biking.models import BikeRide


class BikeRideSerializer(serializers.ModelSerializer):
    ride_avg_km = serializers.FloatField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    modified_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = BikeRide
        fields = ('id', 'ride_km', 'ride_avg_km', 'ride_time', 'ride_wind', 'created_date', 'modified_date',
                  'kcal', 'avg_heartbeat')

    def create(self, validated_data):
        instance = super(BikeRideSerializer, self).create(validated_data)
        instance.ride_avg_km = (instance.ride_km / instance.ride_time) * 60
        instance.save()

        return instance

    def update(self, instance, validated_data):
        instance = super(BikeRideSerializer, self).update(instance, validated_data)
        instance.ride_avg_km = (instance.ride_km / instance.ride_time) * 60
        instance.save()

        return instance