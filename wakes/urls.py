from wakes.views import member_new, wake_new, wake_detail, wake_edit, wake_classic, wake_delete, member, member_new, member_new_list, member_edit_list, member_delete_list, member_edit, member_delete
from django.urls import path




urlpatterns = [
    path('new/', wake_new, name='wake_new'),
    path('<int:wake_id>/', wake_detail, name='wake_detail'),
    path('<int:wake_id>/delete/', wake_delete, name='wake_delete'),
    path('<int:wake_id>/edit/', wake_edit, name='wake_edit'),
    path('classic/', wake_classic, name='wake_classic'),
    path('member/', member, name='member'),
    path('member/member_new', member_new, name="member_new"),
    path('member/member_new_list', member_new_list, name="member_new_list"),
    path('member/edit/member_list', member_edit_list, name="member_edit_list"),
    path('member/delete/member_list', member_delete_list, name="member_delete_list"),
    path('member/<int:member_id>/edit', member_edit, name="member_edit"),
    path('member/<int:member_id>/delete', member_delete, name="member_delete"),

]