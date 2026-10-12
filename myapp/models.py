from django.db import models

class Patient(models.Model):
  name = models.CharField(max_length=200)
  mobile = models.CharField(max_length=10)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=200)
  age = models.IntegerField()
  address = models.CharField(max_length=500)

  def __str__(self):
    return self.name

class Doctor(models.Model):
  name = models.CharField(max_length=200)
  specialization = models.CharField(max_length=200)
  mobile = models.IntegerField()
  email = models.CharField(max_length=200)
  password = models.CharField(max_length=500)
  available = models.BooleanField(default=True)

  def __str__(self):
    return self.name
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("rejected", "Rejected"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        default="pending"
    )
    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    medicine = models.TextField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"