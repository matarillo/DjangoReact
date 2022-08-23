from django.urls import path, include
from rest_framework import routers
from kindergarten.views import ListUsers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users', ListUsers.as_view()),
]
