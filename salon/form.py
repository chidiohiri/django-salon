from django import forms
from .models import Service, ScheduleAppointment, CustomerFeedback

class ScheduleAppointmentForm(forms.ModelForm):
    class Meta:
        model = ScheduleAppointment
        exclude = ('timestamp', 'user', 'total_amount', 'is_verified')

class UpdateAppointmentForm(forms.ModelForm):
    class Meta:
        model = ScheduleAppointment
        exclude = ('timestamp', 'user', 'total_amount', 'is_verified', 'service')

class CustomerFeedbackForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedback
        fields = ['ratings', 'comment']