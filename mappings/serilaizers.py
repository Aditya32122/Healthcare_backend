from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientListSerializer
from doctors.serializers import DoctorListSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_details = PatientListSerializer(source='patient', read_only=True)
    doctor_details = DoctorListSerializer(source='doctor', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        read_only_fields = ('assigned_date',)

class CreateMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ('patient', 'doctor')
    
    def validate(self, attrs):
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')
        
        # Check if mapping already exists
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor, is_active=True).exists():
            raise serializers.ValidationError("This patient is already assigned to this doctor")
        
        return attrs
