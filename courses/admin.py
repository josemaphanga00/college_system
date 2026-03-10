from django.contrib import admin
from .models import Department, Course, Classroom

# @admin.register(Department)
# class Department(admin.ModelAdmin):
#     list_display = ("name", "created_at", "updated_at")
#     search_fields = ("name",)
#     readonly_fields = ("created_at", "updated_at")
#     ordering = ("name",)

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ("department",)
#     search_fields = ("name", "code")
#     readonly_fields = ("created_at", "updated_at")
#     ordering = ("code",)

# @admin.register(Classroom)
# class ClassroomAdmin(admin.ModelAdmin):
#     list_display = ("name", "course", "teacher", "academic_year", "created_at")
#     list_filter = ("course", "teacher", "academic_year")
#     search_fields = ("name", "course_name", "teacher_username")
#     readonly_fields = ("created_at", "updated_at")
#     ordering = ("course", "name")


admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Classroom)