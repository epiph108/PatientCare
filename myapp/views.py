from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import make_password, check_password
import re

def patient_register(request):
    # Logged-in patient cannot register another patient
    if request.session.get('patient_id'):
        return redirect('patient_home')
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            password = request.POST.get('password')
            age = request.POST.get('age')
            address = request.POST.get('address')

            # Required field validation
            if not name or not mobile or not email or not password or not age:
                messages.error(
                    request,
                    "Please fill all required fields"
                )
                return render(
                    request,
                    'patient_register.html'
                )

            # Mobile number validation
            if not re.fullmatch(r"[0-9]{10}", mobile):
                messages.error(
                    request,
                    "Please enter a valid 10-digit mobile number."
                )
                return render(
                    request,
                    "patient_register.html"
                )

            # Email already exists
            if Patient.objects.filter(email=email).exists():
                messages.error(
                    request,
                    "Email already exists"
                )
                return render(
                    request,
                    "patient_register.html"
                )

            patient = Patient.objects.create(
                name=name,
                mobile=mobile,
                email=email,
                password=make_password(password),
                age=age,
                address=address
            )

            request.session['patient_id'] = patient.id

            messages.success(
                request,
                "Registration successful"
            )

            return redirect('patient_home')

        except Exception as e:

            messages.error(
                request,
                f"Registration failed: {str(e)}"
            )

            return render(
                request,
                "patient_register.html"
            )

    return render(
        request,
        "patient_register.html"
    )

def log(request):

    if request.method == "POST":

        try:
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = Patient.objects.filter(email=email).first()

            if user and check_password(password, user.password):

                request.session['patient_id'] = user.id

                messages.success(
                    request,
                    "Login successful"
                )

                return redirect('patient_home')

            else:

                messages.error(
                    request,
                    "Invalid email or password"
                )

        except Exception as e:

            messages.error(
                request,
                f"Login failed: {str(e)}"
            )

    return render(
        request,
        "login.html"
    )


def logout_patient(request):

    request.session.flush()

    messages.success(
        request,
        "Logged out successfully"
    )

    return redirect('login')


def patient_home(request):

    patient_id = request.session.get('patient_id')

    if not patient_id:

        messages.error(
            request,
            "Please login first"
        )

        return redirect('login')

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )

    context = {
        'patient_name': patient.name
    }

    return render(
        request,
        'patient_home.html',
        context
    )


def doctors(request):

    patient_id = request.session.get('patient_id')

    if not patient_id:

        messages.error(
            request,
            "Please login first"
        )

        return redirect('login')

    doctors = Doctor.objects.filter(
        available=True
    )

    context = {
        'doctors': doctors
    }

    return render(
        request,
        'doctors.html',
        context
    )



def book_appointment(request, doctor_id):

    patient_id = request.session.get('patient_id')

    if not patient_id:

        messages.error(
            request,
            "Please login first"
        )

        return redirect('login')

    doctor = get_object_or_404(
        Doctor,
        id=doctor_id,
        available=True
    )

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )

    if request.method == "POST":

        appointment_date = request.POST.get(
            'appointment_date'
        )

        if not appointment_date:

            messages.error(
                request,
                "Please select appointment date and time"
            )

            return render(
                request,
                "book_appointment.html",
                {"doctor": doctor}
            )

        # Prevent double booking
        existing_appointment = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=appointment_date,
            status__in=["pending", "confirmed"]
        ).exists()

        if existing_appointment:

            messages.error(
                request,
                "This doctor is already booked for the selected date and time."
            )

            return render(
                request,
                "book_appointment.html",
                {"doctor": doctor}
            )

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            appointment_date=appointment_date,
            status="pending"
        )

        messages.success(
            request,
            "Appointment booked successfully"
        )

        return redirect('patient_home')

    return render(
        request,
        "book_appointment.html",
        {"doctor": doctor}
    )


def my_appointments(request):

    patient_id = request.session.get('patient_id')

    if not patient_id:

        messages.error(
            request,
            "Please login first"
        )

        return redirect('login')

    appointments = Appointment.objects.filter(
        patient_id=patient_id
    ).select_related(
        'doctor'
    ).order_by(
        '-appointment_date'
    )

    context = {
        'appointments': appointments
    }

    return render(
        request,
        "my_appointments.html",
        context
    )


def doctor_login(request):

    if request.method == "POST":

        try:

            email = request.POST.get('email')
            password = request.POST.get('password')

            doctor = Doctor.objects.filter(
                email=email
            ).first()

            if doctor and check_password(password, doctor.password):

                request.session['doctor_id'] = doctor.id

                messages.success(
                    request,
                    "Doctor login successful"
                )

                return redirect(
                    'doctor_dashboard'
                )

            else:

                messages.error(
                    request,
                    "Invalid email or password"
                )

        except Exception as e:

            messages.error(
                request,
                f"Login failed: {str(e)}"
            )

    return render(
        request,
        "doctor_login.html"
    )



    if request.method == "POST":

        try:

            email = request.POST.get('email')
            password = request.POST.get('password')

            doctor = Doctor.objects.filter(
                email=email
            ).first()

            if doctor and check_password(password, doctor.password):

                request.session['doctor_id'] = doctor.id

                messages.success(
                    request,
                    "Doctor login successful"
                )

                return redirect(
                    'doctor_dashboard'
                )

            else:

                messages.error(
                    request,
                    "Invalid email or password"
                )

        except Exception as e:

            messages.error(
                request,
                f"Login failed: {str(e)}"
            )

    return render(
        request,
        "doctor_login.html"
    )
def logout_doctor(request):

    request.session.flush()

    messages.success(
        request,
        "Logged out successfully"
    )

    return redirect('doctor_login')



def doctor_dashboard(request):

    doctor_id = request.session.get('doctor_id')

    if not doctor_id:

        messages.error(
            request,
            "Please login first"
        )

        return redirect('doctor_login')

    doctor = get_object_or_404(
        Doctor,
        id=doctor_id
    )

    appointments = Appointment.objects.filter(
        doctor=doctor
    ).select_related(
        'patient'
    ).order_by(
        '-appointment_date'
    )

    context = {
        'doctor': doctor,
        'appointments': appointments
    }

    return render(
        request,
        "doctor_dashboard.html",
        context
    )


def accept_appointment(request, appointment_id):

    doctor_id = request.session.get('doctor_id')

    if not doctor_id:

        messages.error(
            request,
            "Please login first"
        )

        return redirect('doctor_login')

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor_id=doctor_id
    )

    appointment.status = "confirmed"
    appointment.save()

    messages.success(
        request,
        "Appointment accepted successfully"
    )

    return redirect(
        'doctor_dashboard'
    )


def reject_appointment(request, appointment_id):

    doctor_id = request.session.get('doctor_id')

    if not doctor_id:

        messages.error(
            request,
            "Please login first"
        )

        return redirect('doctor_login')

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor_id=doctor_id
    )

    appointment.status = "rejected"
    appointment.save()

    messages.success(
        request,
        "Appointment rejected"
    )

    return redirect(
        'doctor_dashboard'
    )


def complete_appointment(request, appointment_id):

    doctor_id = request.session.get('doctor_id')

    if not doctor_id:

        messages.error(
            request,
            "Please login first"
        )

        return redirect('doctor_login')

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor_id=doctor_id
    )

    if appointment.status != "confirmed":

        messages.error(
            request,
            "Only confirmed appointments can be completed"
        )

        return redirect(
            'doctor_dashboard'
        )

    appointment.status = "completed"
    appointment.save()

    messages.success(
        request,
        "Appointment marked as completed"
    )

    return redirect(
        'doctor_dashboard'
    )


def add_medical_record(request, appointment_id):

    doctor_id = request.session.get('doctor_id')

    if not doctor_id:

        messages.error(
            request,
            "Please login first"
        )

        return redirect('doctor_login')

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor_id=doctor_id,
        status="completed"
    )

    if request.method == "POST":

        diagnosis = request.POST.get('diagnosis')
        medicine = request.POST.get('medicine')
        notes = request.POST.get('notes')

        if not diagnosis or not medicine:

            messages.error(
                request,
                "Diagnosis and medicine are required"
            )

            return render(
                request,
                "add_medical_record.html",
                {
                    "appointment": appointment
                }
            )

        MedicalRecord.objects.create(
            patient=appointment.patient,
            doctor=appointment.doctor,
            diagnosis=diagnosis,
            medicine=medicine,
            notes=notes
        )

        messages.success(
            request,
            "Medical record added successfully"
        )

        return redirect(
            'doctor_dashboard'
        )

    return render(
        request,
        "add_medical_record.html",
        {
            "appointment": appointment
        }
    )


def my_medical_records(request):

    patient_id = request.session.get('patient_id')

    if not patient_id:

        messages.error(
            request,
            "Please login first"
        )

        return redirect('login')

    records = MedicalRecord.objects.filter(
        patient_id=patient_id
    ).select_related(
        'doctor'
    ).order_by(
        '-created_at'
    )

    context = {
        'records': records
    }

    return render(
        request,
        "my_medical_records.html",
        context
    )
