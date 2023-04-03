from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=250, validators=[
        RegexValidator(regex='^(?=.*[a-zA-Z ])[a-zA-Z0-9 ]+$', message='Name must contain only letters and spaces.')])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=250, validators=[
        RegexValidator(regex='^(?=.*[a-zA-Z ])[a-zA-Z0-9 ]+$', message='Name must contain only letters and spaces.')])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subcategory


class Course(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    course = models.CharField(max_length=250, validators=[
        RegexValidator(regex='^(?=.*[a-zA-Z ])[a-zA-Z0-9 ]+$', message='Name must contain only letters and spaces.')])
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('course_table')

    def __str__(self):
        return self.course


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topics = models.CharField(max_length=250, validators=[
        RegexValidator(regex='^(?=.*[a-zA-Z ])[a-zA-Z0-9 ]+$', message='Name must contain only letters and spaces.')])
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('topic_table')
