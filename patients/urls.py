from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_patient, name='create_patient'),
    path('list/', views.list_patients, name='list_patients'),
    path('<int:patient_id>/', views.get_patient, name='get_patient'),
    path('<int:patient_id>/update/', views.update_patient, name='update_patient'),
    path('<int:patient_id>/delete/', views.delete_patient, name='delete_patient'),
]