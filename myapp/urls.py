from django.urls import path
from django.shortcuts import redirect
from .views import *


def home_redirect(request):
    return redirect('login')


urlpatterns = [

    path(
        '',
        view=home_redirect,
        name='home'
    ),

    path(
        'register/',
        view=patient_register,
        name='patient_register'
    ),

    path(
        'login/',
        view=log,
        name='login'
    ),


    path(
        'home/',
        view=patient_home,
        name='patient_home'
    ),

    path(
        'logout/',
        view=logout_patient,
        name='logout'
    ),

    path(
        'doctors/',
        view=doctors,
        name='doctors'
    ),

    path(
        'book-appointment/<int:doctor_id>/',
        view=book_appointment,
        name='book_appointment'
    ),

    path(
        'my-appointments/',
        view=my_appointments,
        name='my_appointments'
    ),

    path(
        'doctor-login/',
        view=doctor_login,
        name='doctor_login'
    ),
    
    path(
        'doctor-logout/',
        view=logout_doctor,
        name='doctor_logout'
    ),

    path(
        'doctor-dashboard/',
        view=doctor_dashboard,
        name='doctor_dashboard'
    ),

    path(
        'accept-appointment/<int:appointment_id>/',
        view=accept_appointment,
        name='accept_appointment'
    ),

    path(
        'reject-appointment/<int:appointment_id>/',
        view=reject_appointment,
        name='reject_appointment'
    ),

    path(
        'complete-appointment/<int:appointment_id>/',
        view=complete_appointment,
        name='complete_appointment'
    ),

    path(
        'add-medical-record/<int:appointment_id>/',
        view=add_medical_record,
        name='add_medical_record'
    ),

    path(
        'my-medical-records/',
        view=my_medical_records,
        name='my_medical_records'
    ),
]