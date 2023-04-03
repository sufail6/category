from django.contrib import admin

from .models import Category, Subcategory, Course, Topic

# Register your models here.
admin.site.register(Category)

admin.site.register(Subcategory)

admin.site.register(Course)

admin.site.register(Topic)


