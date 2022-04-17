from django.urls import path, include

from todos.views import TodoViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('', TodoViewSet)

urlpatterns = [
    path('', include(router.urls))
]