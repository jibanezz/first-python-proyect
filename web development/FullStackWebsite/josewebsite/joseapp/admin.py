from django.contrib import admin

# Register your models here.

from .models import Fruit,Student,Alumni


admin.site.register(Fruit)
admin.site.register(Student)

admin.site.register(Alumni)