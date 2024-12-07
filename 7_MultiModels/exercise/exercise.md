# Enhancing the Course Management API

## Exercise Challenge

This exercise involves extending the current Course Management API with new features and enhancements.

---

### **1. Add Token-Based Authentication  IF YOU DIDN'T DO AT FIRST PLACE**
- Implement token-based authentication using Django REST Framework's `rest_framework.authtoken` package.
- Ensure that users need to authenticate to access or modify any course-related data.

---

### **2. Enhancing the API**

#### **Title: Adding Endpoints for Relationships**

**Tasks:**  
1. Fetch courses created by a user.
2. Fetch courses a user is enrolled in.

**Code Snippets:**  
```python
1) Fetch courses created by a user. 

EXAMPLE VIEW CODE : 
@action(detail=False, methods=['get'], url_path='created-by')
def created_by_user(self, request):
    courses = self.queryset.filter(created_by=request.user)
    serializer = self.get_serializer(courses, many=True)
    return Response(serializer.data)

DO SAME FOR 2) Fetch courses a user is enrolled in.

```

---

### **3. Querying the Data**

#### **Title: Practical Queries Using Django ORM**

**Tasks:**  
1. Fetch all courses created by a user:
   ```python
   user = User.objects.get(username='john')
   created_courses = user.created_courses.all()
   ```
2. Fetch all users enrolled in a course:
   ```python
   course = Course.objects.get(title='Python 101')
   enrolled_users = course.users.all()
   ```

---

### **4. Filtering Data**

#### **Title: Adding Filters to Enhance Queries**

**Tasks:**  
1. Filter by date:
   ```python
   from django.utils.timezone import now
   courses = Course.objects.filter(created_date__month=now().month)
   ```
2. Fetch courses with a specific user enrolled:
   ```python
   courses = Course.objects.filter(users__username='john')
   ```

---

## Submission

After implementing the enhancements, test the API thoroughly. Ensure proper documentation and comments are added for all new changes.