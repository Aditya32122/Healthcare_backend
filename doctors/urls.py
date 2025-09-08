from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_doctor, name='create_doctor'),
    path('list/', views.list_doctors, name='list_doctors'),
    path('<int:doctor_id>/', views.get_doctor, name='get_doctor'),
    path('<int:doctor_id>/update/', views.update_doctor, name='update_doctor'),
    path('<int:doctor_id>/delete/', views.delete_doctor, name='delete_doctor'),
]