from django.contrib import admin
from .models import Question,Choice,user

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(user)

# Register your models here.
