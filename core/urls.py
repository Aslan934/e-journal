from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()

router.register(r'students', views.StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
