from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model for the College Administrative System.
    """

    # Role choices
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TEACHER = "TEACHER", "Teacher"

    # Role field to distinguish Admin vs Teacher
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.TEACHER,
        help_text="Defines the role of the user within the system"
    )

    # Account & audit fields
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Helper methods for easy role checking
    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_teacher(self):
        return self.role == self.Role.TEACHER

    def __str__(self):
        return f"{self.username} ({self.role})"