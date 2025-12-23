from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

# Customize admin panel
admin.site.site_header = "University Admin Panel"
admin.site.site_title = "University Admin Portal"
admin.site.index_title = "Welcome to the Admin Dashboard"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matric_number', 'first_name', 'last_name', 'course', 'email')
    search_fields = ('matric_number', 'first_name', 'last_name', 'email')

