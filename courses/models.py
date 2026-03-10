from django.db import models
from users.models import User

class Department(models.Model):
    """
    Department e.g Computer Science, Math, Biotechnology
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Department name"
        )
    
    description = models.TextField(
        blank=True,
        help_text="Optional description of the department"
    )

    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "1. Departments"
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class Course(models.Model):
    """
    Courses Offered within a department
    """

    name = models.CharField(max_length=100,
                            help_text="Course name",

    )
    code = models.CharField(max_length=20,
                            unique=True,
                            help_text="Course code"
    )

    # Relationship to Department
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name="course",
                                   help_text="Department this course belongs to"
    )

    # Audit fields
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "2. Courses"
        ordering = ["code"]

    def __init__(self):
        return f"{self.code} - {self.name}"
    
class Classroom(models.Model):
    """
    Classroom of a course taught by a teacher
    """

    name = models.CharField(max_length=100,
                            help_text="Classroom name",                 
    )

    # Relationship
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name="classrooms",
                               help_text="Course this classroom belongs to"
    )
    teacher = models.ForeignKey(User,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                limit_choices_to={"role": "TEACHER"},
                                related_name="classrooms",
                                help_text="Teacher assigned to this classroom"
    )

    # Optional academic year field
    academic_year = models.CharField(max_length=9,
                                     help_text="Academic year e.g., 2026"                                
    )

    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Classroom"
        verbose_name_plural = "3. Classrooms"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.course.code}) - ({self.academic_year})"
        