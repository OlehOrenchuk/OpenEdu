from django.contrib import admin
from .models import Articles, StudentsGroup, Lesson, Profile, Document

admin.site.register(Articles)
admin.site.register(StudentsGroup)
admin.site.register(Lesson)
admin.site.register(Profile)
admin.site.register(Document)