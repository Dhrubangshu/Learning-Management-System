from django.contrib import admin


# Register your models here.
from .models import Student, Faculty, Course
from import_export.admin import ImportExportModelAdmin
 

@admin.register(Student)
class ViewAdmin(ImportExportModelAdmin):
    pass
#list_display = ("student_id, name, semester")
#class StudentAdmin(admin.ModelAdmin):
    #list_display = ("student_id, name, semester")
   

#admin.site.register(StudentAdmin)
admin.site.register(Faculty)
admin.site.register(Course)
 
