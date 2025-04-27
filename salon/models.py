from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Service(models.Model):
    title = models.CharField(max_length=100) 
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

class ScheduleAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.DateField()
    comment = models.CharField(max_length=400, null=True, blank=True)
    service = models.ManyToManyField(Service)
    timestamp = models.DateTimeField(auto_now_add=True)
    total_amount = models.PositiveIntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    has_rating = models.BooleanField(default=False)

class CustomerFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ratings = models.CharField(
        max_length=30, 
        choices=(
            ('Bad', 'Bad'), 
            ('Good', 'Good'), 
            ('Amazing', 'Amazing')
        )
    )
    comment = models.CharField(max_length=400, null=True, blank=True) 
    appointment = models.OneToOneField(ScheduleAppointment, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


