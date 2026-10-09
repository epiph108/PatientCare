# Doctor Patient Management System

A simple web app built with Django where patients can register, find doctors and book appointments, and doctors can accept or reject those appointments and add medical records after the visit.

## Table of Contents

- [1. Introduction](#1-introduction)
  - [1.1 Features](#11-features)
  - [1.2 Tech Stack](#12-tech-stack)
- [2. Getting Started](#2-getting-started)
  - [2.1 Prerequisites](#21-prerequisites)
  - [2.2 Installation](#22-installation)
  - [2.3 Seed Demo Data](#23-seed-demo-data)
  - [2.4 Run the Server](#24-run-the-server)
- [3. Usage](#3-usage)
  - [3.1 Demo Credentials](#31-demo-credentials)
  - [3.2 Patient Flow](#32-patient-flow)
  - [3.3 Doctor Flow](#33-doctor-flow)
- [4. Project Structure](#4-project-structure)
- [5. Database Models](#5-database-models)
- [6. URL Routes](#6-url-routes)

---

## 1. Introduction

### 1.1 Features

- Patient registration, login and logout
- Browse available doctors
- Book an appointment with a doctor (double booking is blocked)
- Track appointment status: pending, confirmed, rejected, completed
- Separate doctor login and dashboard
- Doctors can accept, reject and complete appointments
- Doctors can add a diagnosis and medicine after a completed appointment
- Doctor logout clears the session fully
- Accept, reject and complete actions use safe POST forms with CSRF token
- Patients can view their medical records
- Django admin panel for managing all data

### 1.2 Tech Stack

- Python
- Django
- SQLite
- HTML and CSS (Django templates)

## 2. Getting Started

### 2.1 Prerequisites

- Python 3.12 or newer
- Git

### 2.2 Installation

```bash
git clone <your-repo-url>
cd <your-repo-folder>

python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

### 2.3 Seed Demo Data

Adds 3 sample doctors and 3 sample patients. It is safe to run more than once.

```bash
python manage.py seed_doctors
python manage.py seed_patients
```

### 2.4 Run the Server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. The admin panel is at http://127.0.0.1:8000/admin/.

## 3. Usage

### 3.1 Demo Credentials

| Role    | Email              | Password  |
| ------- | ------------------ | --------- |
| Patient | riya@example.com   | demo123   |
| Patient | arjun@example.com  | demo123   |
| Patient | meera@example.com  | demo123   |
| Doctor  | rahul@example.com  | doctor123 |
| Doctor  | priya@example.com  | doctor123 |
| Doctor  | amit@example.com   | doctor123 |

Doctors log in at `/doctor-login/`, patients at `/login/`.

### 3.2 Patient Flow

1. Register or log in.
2. Open **Doctors** and pick a doctor.
3. Choose a date and time and book the appointment.
4. Check the status under **My Appointments**.
5. After the visit, open **Medical Records** to see the diagnosis and medicine.

### 3.3 Doctor Flow

1. Log in from the doctor login page.
2. Open the dashboard and review the appointment requests.
3. Accept or reject a pending appointment.
4. Mark a confirmed appointment as completed.
5. Add the diagnosis, medicine and notes for the patient.

## 4. Project Structure

```
.
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── myproject/              # project settings and root URLs
└── myapp/
    ├── models.py           # Patient, Doctor, Appointment, MedicalRecord
    ├── views.py            # all views
    ├── urls.py             # app routes
    ├── admin.py
    ├── templates/          # HTML templates
    ├── migrations/
    └── management/
        └── commands/
            ├── seed_doctors.py
            └── seed_patients.py
```

## 5. Database Models

| Model         | Main fields                                                                  |
| ------------- | ---------------------------------------------------------------------------- |
| Patient       | name, mobile, email, password, age, address                                  |
| Doctor        | name, specialization, mobile, email, password, address, available            |
| Appointment   | patient, doctor, appointment_date, status                                    |
| MedicalRecord | patient, doctor, diagnosis, medicine, notes, created_at                      |

Appointment status can be `pending`, `confirmed`, `rejected`, `completed` or `cancelled`.

## 6. URL Routes

| URL                                  | Who     | Purpose                      |
| ------------------------------------ | ------- | ---------------------------- |
| `/register/`                         | Patient | Create an account            |
| `/login/`                            | Patient | Log in                       |
| `/home/`                             | Patient | Patient home                 |
| `/doctors/`                          | Patient | List available doctors       |
| `/book-appointment/<doctor_id>/`     | Patient | Book an appointment          |
| `/my-appointments/`                  | Patient | View own appointments        |
| `/my-medical-records/`               | Patient | View own medical records     |
| `/logout/`                           | Patient | Log out                      |
| `/doctor-login/`                     | Doctor  | Log in                       |
| `/doctor-dashboard/`                 | Doctor  | View appointments            |
| `/accept-appointment/<id>/`          | Doctor  | Accept an appointment        |
| `/reject-appointment/<id>/`          | Doctor  | Reject an appointment        |
| `/complete-appointment/<id>/`        | Doctor  | Mark as completed            |
| `/add-medical-record/<id>/`          | Doctor  | Add a medical record         |
| `/doctor-logout/`                    | Doctor  | Log out                      |
| `/admin/`                            | Admin   | Django admin panel           |
