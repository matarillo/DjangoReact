from django.urls import path, include
from rest_framework import routers
from kindergarten.views import ClassViewSet, ListUsers

router = routers.DefaultRouter()
router.register(r'class', ClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users', ListUsers.as_view()),
]
