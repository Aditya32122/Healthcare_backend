from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_mapping, name='create_mapping'),
    path('list/', views.list_mappings, name='list_mappings'),
    path('<int:patient_id>/', views.get_patient_doctors, name='get_patient_doctors'),
    path('<int:mapping_id>/remove/', views.remove_mapping, name='remove_mapping'),
]