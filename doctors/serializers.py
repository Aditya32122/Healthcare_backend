from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate_consultation_fee(self, value):
        if value < 0:
            raise serializers.ValidationError("Consultation fee cannot be negative")
        return value

    def validate_years_of_experience(self, value):
        if value < 0 or value > 70:
            raise serializers.ValidationError("Years of experience must be between 0 and 70")
        return value

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'name', 'specialization', 'hospital_affiliation', 'consultation_fee')