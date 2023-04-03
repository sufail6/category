from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.core import validators
from .models import *


class Items(forms.ModelForm):
    category_name = forms.CharField(
        required=False,
        error_messages={'required': 'The category name field is required.'}
    )

    class Meta:
        model = Category
        fields = '__all__'

    def clean_category_name(self):
        category_name = self.cleaned_data['category_name']
        if not category_name:
            raise ValidationError('def')
        return category_name


class Field(forms.ModelForm):
    subcategory = forms.CharField(
        required=False,
        error_messages={'required': 'The category name field is required.'}
    )

    def clean_subcategory(self):
        subcategory = self.cleaned_data['subcategory']
        if not subcategory:
            raise ValidationError('def')
        return subcategory

    def __init__(
            self,
            data=None,
            files=None,
            auto_id="id_%s",
            prefix=None,
            initial=None,
            error_class=ErrorList,
            label_suffix=None,
            empty_permitted=False,
            instance=None,
            use_required_attribute=None,
            renderer=None,
    ):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        self.is_active = None

    class Meta:
        model = Subcategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Field, self).__init__(*args, **kwargs)
        self.fields['category_name'].queryset = Category.objects.order_by('-id')


class CourseForm(forms.ModelForm):
    course = forms.CharField(
        required=False,
        error_messages={'required': 'The category name field is required.'}
    )

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Subcategory.objects.order_by('-id')

    def clean_course(self):
        course = self.cleaned_data['course']
        if not course:
            raise ValidationError('def')
        return course


class TopicForm(forms.ModelForm):
    topics = forms.CharField(
        required=False,
        error_messages={'required': 'The category name field is required.'}
    )

    class Meta:
        model = Topic
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.order_by('-id')

    def clean_topics(self):
        topics = self.cleaned_data['topics']
        if not topics:
            raise ValidationError('def')
        return topics
