from django.urls import path 
from . import views 

urlpatterns = [
    path('schedule-appointment/', views.schedule_appointment, name='schedule-appointment'),
    path('update-appointment/<int:pk>/', views.update_appointment, name='update-appointment'), 
    path('my-appointments/', views.my_appointments, name='my-appointments'), 
    path('salon-appointments/', views.salon_appointments, name='salon-appointments'), 
    path('delete-appointment/<int:pk>/', views.delete_appointment, name='delete-appointment'), 
    path('service-feedback/<int:pk>/', views.service_feedback, name='service-feedback'), 
]