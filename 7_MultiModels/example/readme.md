
# Course Management API

## Overview

This project is a Django-based REST API for managing courses and user enrollments. It includes features like CRUD operations for courses, and relationships between users and courses.

---

## Features

1. **Courses:**
   - CRUD functionality (Create, Read, Update, Delete).
2. **Relationships:**
   - **Many-to-Many:** A user can enroll in multiple courses.
   - **One-to-Many:** A user can create multiple courses.

---

## Setup Instructions


### **1. Create the Django Project**
- Initialize the Django project:
  ```bash
  django-admin startproject course_api
  cd course_api
  ```
- Install the required packages:
  ```bash
  pip install djangorestframework mysqlclient
  ```

### **2. Configure the Database**
- Update `settings.py`:
  - Add required apps:
    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'api',
    ]
    ```
  - Configure MySQL as the database:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

---

### **ADD AUTHENTICATION FIRST BY YOURSELF., USE EXAMPLE CODE IN BACKEND**



## NEXT Implementation Steps

### **1. Define Models**
In `api/models.py`:
```python
from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_courses")
    users = models.ManyToManyField(User, related_name="enrolled_courses", blank=True)

    def __str__(self):
        return self.title
```

### **2. Create Serializers**
In `api/serializers.py`:
```python
from rest_framework import serializers
from .models import Course
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CourseSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_by', 'users']
```

---

### **3. Create Viewsets**
In `api/views.py`:
```python
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
from rest_framework.decorators import action

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None):
        course = self.get_object()
        course.users.add(request.user)
        course.save()
        return Response({'status': 'enrolled successfully'})

    @action(detail=True, methods=['post'])
    def unenroll(self, request, pk=None):
        course = self.get_object()
        course.users.remove(request.user)
        course.save()
        return Response({'status': 'unenrolled successfully'})
```

---

### **4. Configure URLs**
- In `api/urls.py`:
  ```python
  from django.urls import path, include
  from rest_framework.routers import DefaultRouter
  from .views import CourseViewSet

  router = DefaultRouter()
  router.register(r'courses', CourseViewSet)

  urlpatterns = [
      path('', include(router.urls)),
  ]
  ```
- In `course_api/urls.py`:
  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/', include('api.urls')),
  ]
  ```

---

### **5. Apply Migrations**
- Run migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- Create a superuser:
  ```bash
  python manage.py createsuperuser
  ```

---

## Testing the API

Use Postman or CURL to test the following endpoints:

1. **Create a Course**  
   POST `/api/courses/`  
   Request Body:
   ```json
   {
       "title": "Sample Course",
       "description": "This is a sample course."
   }
   ```

2. **Retrieve All Courses**  
   GET `/api/courses/`

3. **Enroll in a Course**  
   POST `/api/courses/<id>/enroll/`

4. **Unenroll from a Course**  
   POST `/api/courses/<id>/unenroll/`

---

## Key Features

- **Many-to-Many (`users`):** Tracks enrolled users for each course.
- **One-to-Many (`created_by`):** Tracks the creator of each course.

This project serves as a robust foundation for building scalable course management systems with Django and DRF. Happy coding!
