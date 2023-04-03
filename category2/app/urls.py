from django.urls import path

from app import views
from app.views import CourseView

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('login_view', views.login_view, name='login_view'),

    path('category_add', views.category_add, name='category_add'),
    path('category_view', views.category_view, name='category_view'),
    path('category_update/<int:id>', views.category_update, name='category_update'),
    path('category_enable/<int:id>', views.category_enable, name='category_enable'),
    path('category_disable/<int:id>', views.category_disable, name='category_disable'),
    path('search/', views.search, name='search'),

    path('sub_add', views.sub_add, name='sub_add'),
    path('sub_view', views.sub_view, name='sub_view'),
    path('search_sub', views.search_sub, name='search_sub'),
    path('sub_update/<int:id>', views.sub_update, name='sub_update'),
    path('sub_enable/<int:id>', views.sub_enable, name='sub_enable'),
    path('sub_disable/<int:id>', views.sub_disable, name='sub_disable'),

    path('course_form/', views.CourseView.as_view(), name='course_form'),
    path('course_table/', views.course_table, name='course_table'),
    path('course_update/<int:pk>/', views.UpdateView.as_view(), name='course_update'),
    path('course_enable/<int:pk>/', views.course_enable, name='course_enable'),
    path('course_disable/<int:pk>/', views.course_disable, name='course_disable'),

    path('topic_form/', views.TopicView.as_view(), name='topic_form'),
    path('topic_table/', views.topic_table, name='topic_table'),
    path('topic_update/<int:pk>/', views.EditView.as_view(), name='topic_update'),
    path('topic_enable/<int:pk>/', views.topic_enable, name='topic_enable'),
    path('topic_disable/<int:pk>/', views.topic_disable, name='topic_disable'),

    path('data', views.data, name='data'),

]
