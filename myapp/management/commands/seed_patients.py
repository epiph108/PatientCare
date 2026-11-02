from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from myapp.models import Patient

class Command(BaseCommand):
    help = 'Seeds the database with sample patients for demo purposes'

    def handle(self, *args, **kwargs):
        sample_patients = [
            {"name": "Riya Sharma", "mobile": "9876543210", "email": "riya@example.com", "password": "demo123", "age": 28, "address": "Mumbai"},
            {"name": "Arjun Patel", "mobile": "9123456780", "email": "arjun@example.com", "password": "demo123", "age": 34, "address": "Ahmedabad"},
            {"name": "Meera Iyer", "mobile": "9988776655", "email": "meera@example.com", "password": "demo123", "age": 45, "address": "Chennai"},
        ]

        for data in sample_patients:
            patient, created = Patient.objects.get_or_create(
                email=data["email"],
                defaults={**data, "password": make_password(data["password"])}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {patient.name}"))
            else:
                self.stdout.write(f"Already exists: {patient.name}")
