import django_filters
from .models import ScheduleAppointment

class AppointmentFilter(django_filters.FilterSet):
    class Meta:
        model = ScheduleAppointment
        fields = [
            'appointment', 'service'
        ]