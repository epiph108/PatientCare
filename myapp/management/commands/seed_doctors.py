from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from myapp.models import Doctor

class Command(BaseCommand):

    help = "Seeds the database with sample doctors for demo purposes"

    def handle(self, *args, **kwargs):

        sample_doctors = [
            {
                "name": "Rahul Sharma",
                "specialization": "Cardiologist",
                "mobile": "9876543211",
                "email": "rahul@example.com",
                "password": "doctor123",
                "address": "Ahmedabad",
                "available": True
            },
            {
                "name": "Priya Mehta",
                "specialization": "Dermatologist",
                "mobile": "9123456781",
                "email": "priya@example.com",
                "password": "doctor123",
                "address": "Mumbai",
                "available": True
            },
            {
                "name": "Amit Patel",
                "specialization": "General Physician",
                "mobile": "9988776656",
                "email": "amit@example.com",
                "password": "doctor123",
                "address": "Ahmedabad",
                "available": True
            },
        ]

        for data in sample_doctors:

            doctor, created = Doctor.objects.get_or_create(
                email=data["email"],
                defaults={**data, "password": make_password(data["password"])}
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created: {doctor.name}"
                    )
                )
            else:
                self.stdout.write(
                    f"Already exists: {doctor.name}"
                )
