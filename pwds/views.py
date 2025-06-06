# pwds/views.py
from django.shortcuts import render, redirect
from .models import PWDProfile
from .forms import PWDProfileForm
from django.contrib.auth.decorators import login_required
from bookings.models import Booking  # add this import
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

@login_required
def dashboard_view(request):
    try:
        profile = PWDProfile.objects.get(user=request.user)
        profile_complete = all([
            profile.contact_number,
            profile.disability_type,
            profile.travel_needs,
        ])

        # ✅ Filter bookings where PWD is the current user
        bookings = Booking.objects.filter(pwd=request.user)

        # ✅ Filter completed bookings to notify arrival
        completed_bookings = bookings.filter(status='Completed')

        return render(request, 'pwds/dashboard.html', {
            'profile': profile,
            'profile_complete': profile_complete,
            'bookings': bookings,
            'completed_bookings': completed_bookings,  # for notification
        })

    except PWDProfile.DoesNotExist:
        return redirect('pwds:edit_profile')

@login_required
def edit_profile_view(request):
    try:
        profile = PWDProfile.objects.get(user=request.user)
    except PWDProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = PWDProfileForm(request.POST, instance=profile)
        if form.is_valid():
            pwd_profile = form.save(commit=False)
            pwd_profile.user = request.user
            pwd_profile.save()
            return redirect('pwds:dashboard')
    else:
        form = PWDProfileForm(instance=profile)
    return render(request, 'pwds/edit_profile.html', {'form': form})

@login_required
def accept_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user == booking.driver.user:
        booking.status = 'Approved'
        booking.save()
        messages.success(request, "You accepted the booking.")
    return redirect('drivers:dashboard')

@login_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user == booking.driver.user:
        booking.status = 'Rejected'
        booking.save()
        messages.warning(request, "You rejected the booking.")
    return redirect('drivers:dashboard')
