from wakes.views import wake_new, wake_detail, wake_edit, wake_classic, member
from django.urls import path




urlpatterns = [
    path('new/', wake_new, name='wake_new'),
    path('<int:wake_id>/', wake_detail, name='wake_detail'),
    path('<int:wake_id>/edit/', wake_edit, name='wake_edit'),
    path('classic/', wake_classic, name='wake_classic'),
    path('member/new/', member, name='member_new'),
]