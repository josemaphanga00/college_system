# College Administrative System

A Django-based system for managing academic data in a structured, secure, and centralized way.
Built to replace scattered spreadsheets and manual record-keeping in educational institutions.

---

## Overview

This project provides a platform for managing:

* Academic structure (**Departments, Courses, Classrooms**)
* Student data and enrollment
* Records such as grades, attendance, and assignments

The system ensures:

* Data integrity
* Easy access and updates
* Clear organization of academic information

## Project Structure

```
users       → Authentication and roles (Admin, Teacher)
academics   → Department, Course, Classroom
students    → Student, Enrollment, Guardian, Documents
records     → Grades, Attendance, Assignments (planned)
core        → Shared logic and utilities
```

## Roles

* **Admin**

  * Full system control
  * Manages users and academic structure

* **Teacher**

  * Manages student data within assigned classes

## Key Features

* Role-based access control
* Centralized academic data management
* Student tracking and history
* Admin dashboard for managing system data


## Setup

```bash
git clone <repo-url>
cd project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Status

In active development — currently building core models and admin interface.


## 📄 License

MIT License
