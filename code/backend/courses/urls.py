from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, RegisterView, loginpost


router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('login', loginpost, name='login_post'),
    path('signup', RegisterView.as_view()),
    path('', include(router.urls))
]
