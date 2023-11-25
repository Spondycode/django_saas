from django.contrib import admin

from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'instructor']
    search_fields = ['title', 'instructor__username']
    list_filter = ['created_at', 'updated_at', 'instructor']
    
