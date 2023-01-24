from django.contrib import admin
from blog.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display=['name','email','mobile']
admin.site.register(Student,StudentAdmin)