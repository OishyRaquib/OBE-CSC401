from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Question)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(User)
admin.site.register(Student)