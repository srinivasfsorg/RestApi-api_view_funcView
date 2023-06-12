from django.contrib import admin
from ApiView.models import  Employs

# Register your models here.
@admin.register(Employs)
class EmpAdmin(admin.ModelAdmin):
    list_display = ['id', 'empid', 'empname', 'salary', 'deptid']