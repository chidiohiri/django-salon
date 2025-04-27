from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Service, ScheduleAppointment, CustomerFeedback
from . import form as fm 
from payment.models import Wallet
from .filters import AppointmentFilter

User = get_user_model()

@login_required
def schedule_appointment(request):
    if request.method == 'POST':
        form = fm.ScheduleAppointmentForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user

            # Calculate total amount from selected services
            service_ids = form.cleaned_data['service'].values_list('id', flat=True)
            selected_services = Service.objects.filter(id__in=service_ids)
            total_price = sum(service.price for service in selected_services)
            var.total_amount = total_price

            # Get wallet and make payment 
            wallet = Wallet.objects.get(user=request.user)

            if wallet.balance < var.total_amount:
                messages.warning(request, 'Wallet balance is low. Please top up')
                return redirect('dashboard')
            
            wallet.balance = wallet.balance - var.total_amount

            var.save()  # Save appointment without m2m yet
            form.save_m2m()  # Save many-to-many service relation
            wallet.save()

            messages.success(request, 'Appointment successful and saved')
            return redirect('my-appointments')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('schedule-appointment')
    else:
        form = fm.ScheduleAppointmentForm()

    context = {'form': form}
    return render(request, 'salon/schedule_appointment.html', context)

@login_required
def update_appointment(request, pk):
    appointment = ScheduleAppointment.objects.get(pk=pk)

    if appointment.user != request.user:
        messages.warning(request, 'You cannot update this appointment, because you did not create it')
        return redirect('dashboard')

    today = timezone.now().date()

    if appointment.appointment <= today:
        messages.warning(request, 'You cannot delete this appointment on the scheduled date')
        return redirect('my-appointments')

    if request.method == 'POST':
        form = fm.UpdateAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment information has been updated and saved')
            return redirect('my-appointments')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('update-appointment', appointment.pk)
    else:
        form = fm.UpdateAppointmentForm(instance=appointment)
        context = {'appointment':appointment, 'form':form} 
    return render(request, 'salon/update_appointment.html', context)

@login_required
def my_appointments(request):
    appointments = ScheduleAppointment.objects.filter(user=request.user).order_by('-timestamp')
    today = timezone.now().date()

    # apply filter 
    appointments_filter = AppointmentFilter(request.GET, queryset=appointments)
    filtered_appointments = appointments_filter.qs

    # pagination
    paginator = Paginator(filtered_appointments, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Add a status property to each appointment
    for a in page_obj:
        appt_date = a.appointment
        if appt_date == today:
            a.status = "today"
        elif appt_date < today:
            a.status = "past"
        else:
            a.status = "upcoming"

    context = {'appointments':page_obj, 'filter':appointments_filter}
    return render(request, 'salon/my_appointments.html', context)

@login_required
def salon_appointments(request):
    appointments = ScheduleAppointment.objects.all()
    context = {'appointments':appointments}
    return render(request, 'salon/salon_appointments.html', context)

@login_required
def delete_appointment(request, pk):
    appointment = ScheduleAppointment.objects.get(pk=pk)
    
    if appointment.user != request.user:
        messages.warning(request, 'You cannot delete this appointment, because you did not create it')
        return redirect('dashboard')

    today = timezone.now().date()

    if appointment.appointment <= today:
        messages.warning(request, 'You cannot delete this appointment on the scheduled date')
        return redirect('my-appointments')
    
    # refund customer back their money
    wallet = Wallet.objects.get(user=request.user)
    wallet.balance = wallet.balance + appointment.total_amount
    wallet.save()

    # delete appointment
    appointment.delete()

    messages.success(request, 'Appointment has been deleted and money refunded back to wallet')
    return redirect('my-appointments')

@login_required
def service_feedback(request, pk):
    appointment = ScheduleAppointment.objects.get(pk=pk)

    if request.method == 'POST':
        form = fm.CustomerFeedbackForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.appointment = appointment
            var.save()
            appointment.has_rating = True
            appointment.save()
            
            messages.success(request, 'Feedback sent to Database')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('service-feedback', appointment.pk)
    else:
        form = fm.CustomerFeedbackForm()
        context = {'form':form, 'appointment':appointment}
    return render(request, 'salon/service_feedback.html', context)

# barber can cancel a day, so customers would not be able to schedule appointments