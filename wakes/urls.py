from wakes.views import wake_new
from django.urls import path




urlpatterns = [
    path('new/', wake_new, name='top'),
]