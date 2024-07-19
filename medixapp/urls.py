
from django.contrib import admin
from django.urls import path
from medixapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('departments/', views.departments, name='departments'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
]
