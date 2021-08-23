from wakes.views import member_new, wake_new, wake_detail, wake_edit, wake_classic, member, member_new
from django.urls import path




urlpatterns = [
    path('new/', wake_new, name='wake_new'),
    path('<int:wake_id>/', wake_detail, name='wake_detail'),
    path('<int:wake_id>/edit/', wake_edit, name='wake_edit'),
    path('classic/', wake_classic, name='wake_classic'),
    path('member/new/', member, name='member'),
    path('member/member_new', member_new, name="member_new"),
    # path('member/member_edit', member_edit, name="member_edit"),
    # path('member/member_delete', member_delete, name="member_delete"),

]