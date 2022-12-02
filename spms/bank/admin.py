from django.contrib import admin

# Register your models here.

from .models import *
admin.site.site_header = 'Student Performance Management System'             
admin.site.index_title = 'Admin'                
admin.site.site_title = 'SPMS 3.0'

admin.site.register(Question)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(CourseOutline)