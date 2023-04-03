from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q, Prefetch
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers

# Create your views here.


# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from pyexpat import model

from app.forms import Items, Field, CourseForm, TopicForm
from app.models import Category, Subcategory, Course, Topic


@login_required
def home(request):
    return render(request, 'home.html')


def category_add(request):
    if request.method == "POST":
        form = Items(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/category_view')
            except:
                pass
        else:
            messages.info(request, '')
    else:
        form = Items()
    return render(request, 'category.html', {'form': form})


#
def category_view(request):
    data = Category.objects.order_by('-id')
    page = Paginator(data, 2)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, 'category_view.html', context)


def search(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        search_query = request.GET.get('q', None)
        if search_query:
            data = Category.objects.filter(category_name__icontains=search_query).order_by('-id')
            results = []
            for category in data:
                category_json = {'id': category.id, 'category_name': category.category_name}
                results.append(category_json)
            return JsonResponse({'data': results})
    return JsonResponse({'data': 'fail'})


def category_update(request, id):
    data = Category.objects.get(id=id)
    if request.method == 'POST':
        form = Items(request.POST or None, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('category_view')
    else:
        form = Items(instance=data)
    return render(request, 'category_update.html', {'form': form})


def category_enable(request, id):
    data = get_object_or_404(Category, id=id)
    if data.is_active == True:
        data.is_active = False
        data.save()
    else:
        pass
    return category_view(request)


def category_disable(request, id):
    data = get_object_or_404(Category, id=id)
    if data.is_active == False:
        data.is_active = True
        data.save()
    else:
        pass
    return category_view(request)


def sub_add(request):
    if request.method == "POST":
        form = Field(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/sub_view')
            except:
                pass
        else:
            messages.info(request, 'Invalid password or username')
    else:
        form = Field()
    return render(request, 'sub_add.html', {'form': form})


decorators = [never_cache, login_required]


# def sub_view(request):
#     if 'w' in request.GET:
#         w = request.GET['w']
#         data = Subcategory.objects.select_related('category_name').filter(subcategory__icontains=w)
#     else:
#         data = Subcategory.objects.select_related('category_name').all().order_by('-id')
#
#     paginator = Paginator(data, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {'data': data, 'page_obj': page_obj}
#     return render(request, 'sub_view.html', context)
# def sub_view(request):
#     search_query = request.GET.get('q', '')
#     data = Subcategory.objects.filter(subcategory__icontains=search_query).order_by('-id')
#     page = Paginator(data, 2)
#     page_list = request.GET.get('page')
#     page = page.get_page(page_list)
#     context = {
#         'page': page,
#         'search_query': search_query,
#     }
#     return render(request, 'sub_view.html', context)

def sub_view(request):
    form = Subcategory.objects.order_by('-id')
    page = Paginator(form, 2)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, 'sub_view.html', context)


# def search_sub(request):
#     if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         search_query = request.GET.get('q', None)
#         if search_query:
#             form = Subcategory.objects.filter(subcategory__icontains=search_query).order_by('-id')
#             results = []
#             for subcategory in form:
#                 subcategory_json = {'id': subcategory.id, 'subcategory': subcategory.subcategory}
#                 results.append(subcategory_json)
#             return JsonResponse({'form': results})
#     return JsonResponse({'form': 'fail'})
def search_sub(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        search_query = request.GET.get('q', None)
        if search_query:
            form = Subcategory.objects.filter(subcategory__icontains=search_query).order_by('-id')
            results = []
            for subcategory in form:
                subcategory_json = {'id': subcategory.id, 'subcategory': subcategory.subcategory}
                results.append(subcategory_json)
            return JsonResponse({'form': results})
    return JsonResponse({'form': 'fail'})


def sub_update(request, id):
    data = Subcategory.objects.get(id=id)
    if request.method == 'POST':
        form = Field(request.POST or None, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('sub_view')
    else:
        form = Field(instance=data)
    return render(request, 'sub_update.html', {'form': form})


def sub_enable(request, id):
    data = get_object_or_404(Subcategory, id=id)
    if data.is_active == True:
        data.is_active = False
        data.save()
    else:
        pass
    return sub_view(request)


def sub_disable(request, id):
    data = get_object_or_404(Subcategory, id=id)
    if data.is_active == False:
        data.is_active = True
        data.save()
    else:
        pass
    return sub_view(request)


@method_decorator(login_required, name='dispatch')
class CourseView(LoginRequiredMixin, View):
    login_url = '/login_view/'
    form_class = CourseForm
    initial = {'key': 'value'}
    template_name = 'course_form.html'

    def get(self, request, ):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_table')
        return render(request, self.template_name, {'form': form})


def course_table(request):
    search_query = request.GET.get('q', '')
    data = Course.objects.select_related('subcategory').filter(course__icontains=search_query).order_by('-id')
    page = Paginator(data, 2)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
        'search_query': search_query,
    }
    return render(request, 'course_table.html', context)


# def course_table(request):
#     search_query = request.GET.get('q', '')
#     data = Course.objects.filter(course__icontains=search_query).order_by('-id')
#     page = Paginator(data, 2)
#     page_list = request.GET.get('page')
#     page = page.get_page(page_list)
#     context = {
#         'page': page,
#         'search_query': search_query,
#     }
#     return render(request, 'course_table.html', context)


class UpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_update.html'


def course_enable(request, pk):
    data = get_object_or_404(Course, pk=pk)
    if data.is_active == True:
        data.is_active = False
        data.save()
    else:
        pass
    return redirect('course_table')


def course_disable(request, pk):
    data = get_object_or_404(Course, pk=pk)
    if data.is_active == False:
        data.is_active = True
        data.save()
    else:
        pass
    return course_table(request)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Password Or Username')

    return render(request, 'login.html')


decorators = [never_cache, login_required]


@method_decorator(login_required, name='dispatch')
class TopicView(View):
    form_class = TopicForm
    initial = {'key': 'value'}
    template_name = 'topic_form.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'invalid input ')
            return redirect('topic_table')
        return render(request, self.template_name, {'form': form})


def topic_table(request):
    search_query = request.GET.get('q', '')
    data = Topic.objects.select_related('course').filter(topics__icontains=search_query).order_by('-id')
    page = Paginator(data, 2)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
        'search_query': search_query,
    }
    return render(request, 'topic_table.html', context)


# def topic_table(request):
#     search_query = request.GET.get('q', '')
#     data = Topic.objects.filter(topics__icontains=search_query).order_by('-id')
#     page = Paginator(data, 2)
#     page_list = request.GET.get('page')
#     page = page.get_page(page_list)
#     context = {
#         'page': page,
#         'search_query': search_query,
#     }
#     return render(request, 'topic_table.html', context)


class EditView(UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = 'topic_update.html'


def topic_enable(request, pk):
    data = get_object_or_404(Topic, pk=pk)
    if data.is_active == True:
        data.is_active = False
        data.save()
    else:
        pass
    return redirect('topic_table')


def topic_disable(request, pk):
    data = get_object_or_404(Topic, pk=pk)
    if data.is_active == False:
        data.is_active = True
        data.save()
    else:
        pass
    return redirect(request)


def logout(request):
    logout(request)
    return redirect('login_view')


def data(request):
    return render(request, 'data.html')
