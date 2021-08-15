from group.views import top
from django.contrib import admin
from django.urls import path
from django.urls.conf import include



urlpatterns = [
    path('/top', top, name='top'),
    path('/group', include('group.urls'), name='group'),
    path('admin/', admin.site.urls),
    
]
