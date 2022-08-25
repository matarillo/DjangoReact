from django.urls import path, include
from rest_framework import routers
from kindergarten.views import ClassViewSet, ChildViewSet, TeacherViewSet, ListUsers

router = routers.DefaultRouter()
router.register(r'class', ClassViewSet)
router.register(r'child', ChildViewSet)
router.register(r'teacher', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users', ListUsers.as_view()),
]
