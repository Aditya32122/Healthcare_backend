# Healthcare Backend API

This project provides RESTful APIs for managing users, patients, doctors, and their mappings.

## Authentication APIs

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login user

## Patient APIs

- `POST /api/patients/` - Create patient
- `GET /api/patients/list/` - List all patients for authenticated user
- `GET /api/patients/<id>/` - Get patient details
- `PUT /api/patients/<id>/update/` - Update patient
- `DELETE /api/patients/<id>/delete/` - Delete patient

## Doctor APIs

- `POST /api/doctors/` - Create doctor
- `GET /api/doctors/list/` - List all doctors
- `GET /api/doctors/<id>/` - Get doctor details
- `PUT /api/doctors/<id>/update/` - Update doctor
- `DELETE /api/doctors/<id>/delete/` - Delete doctor

## Mapping APIs

- `POST /api/mappings/` - Create patient-doctor mapping
- `GET /api/mappings/list/` - List all mappings for authenticated user
- `GET /api/mappings/<patient_id>/` - Get doctors for specific patient
- `DELETE /api/mappings/<id>/remove/` - Remove mapping