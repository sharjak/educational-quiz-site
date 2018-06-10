from django.contrib import admin

from .models import Answer, Theme, Quiz, Question

# Register your models here.
admin.site.register(Theme)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Quiz)
