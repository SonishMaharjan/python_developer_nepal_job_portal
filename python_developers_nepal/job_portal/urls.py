from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'company', views.CompanyViewSet)
router.register(r'intern-post', views.InternPostViewSet)
router.register(r'job-post', views.JobPostViewSet)


urlpatterns = [
    path('', include(router.urls))
]