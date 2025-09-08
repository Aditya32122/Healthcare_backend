from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Patient
from .serializers import PatientSerializer, PatientListSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response({
            'message': 'Patient created successfully',
            'patient': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_patients(request):
    patients = Patient.objects.filter(created_by=request.user)
    serializer = PatientListSerializer(patients, many=True)
    return Response({
        'count': patients.count(),
        'patients': serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
    serializer = PatientSerializer(patient)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
    serializer = PatientSerializer(patient, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Patient updated successfully',
            'patient': serializer.data
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
    patient.delete()
    return Response({
        'message': 'Patient deleted successfully'
    }, status=status.HTTP_200_OK)