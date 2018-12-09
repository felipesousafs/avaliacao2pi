from django.contrib import admin
from pools.models import Question, Choice, Category
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Category)