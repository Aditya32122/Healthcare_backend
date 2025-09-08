from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from patients.models import Patient
from .serilaizers import PatientDoctorMappingSerializer, CreateMappingSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_mapping(request):
    serializer = CreateMappingSerializer(data=request.data)
    if serializer.is_valid():
        # Ensure the patient belongs to the authenticated user
        patient = serializer.validated_data['patient']
        if patient.created_by != request.user:
            return Response({
                'error': 'You can only assign doctors to your own patients'
            }, status=status.HTTP_403_FORBIDDEN)
        
        mapping = serializer.save()
        response_serializer = PatientDoctorMappingSerializer(mapping)
        return Response({
            'message': 'Patient-Doctor mapping created successfully',
            'mapping': response_serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_mappings(request):
    # Only show mappings for patients created by the authenticated user
    mappings = PatientDoctorMapping.objects.filter(
        patient__created_by=request.user,
        is_active=True
    )
    serializer = PatientDoctorMappingSerializer(mappings, many=True)
    return Response({
        'count': mappings.count(),
        'mappings': serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patient_doctors(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
    mappings = PatientDoctorMapping.objects.filter(patient=patient, is_active=True)
    serializer = PatientDoctorMappingSerializer(mappings, many=True)
    return Response({
        'patient': patient.name,
        'assigned_doctors': serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_mapping(request, mapping_id):
    mapping = get_object_or_404(PatientDoctorMapping, id=mapping_id)
    
    # Ensure the patient belongs to the authenticated user
    if mapping.patient.created_by != request.user:
        return Response({
            'error': 'You can only manage mappings for your own patients'
        }, status=status.HTTP_403_FORBIDDEN)
    
    mapping.is_active = False
    mapping.save()
    
    return Response({
        'message': 'Patient-Doctor mapping removed successfully'
    }, status=status.HTTP_200_OK)