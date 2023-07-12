from django.contrib import admin
from .models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id','question','answer']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Quiz,QuizAdmin)