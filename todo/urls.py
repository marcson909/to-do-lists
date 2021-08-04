from django.urls import path, include
from .views import current_user, UserList, TaskViewSet, ListViewSet
from rest_framework_nested import routers
# from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', ListViewSet, basename='lists')
# router.register(r'tasks', TaskViewSet, basename='tasks')

tasks_router = routers.NestedSimpleRouter(router, r'', lookup='list')
tasks_router.register(r'tasks', TaskViewSet, basename='tasks')


urlpatterns = [
        path('current_user/', current_user),
        path('users/', UserList.as_view()),
        path('', include(router.urls)),
        path('', include(tasks_router.urls)),
    ]
