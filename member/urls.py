from member.views import member_new, member_new, member_new_list, member_edit_list, member_delete_list, member_edit, member_delete, member
from django.urls import path

app_name = 'member'

urlpatterns = [
    #一覧
    path('', member, name="member"),

    # フォーム用ルーティング
    path('member_new_list', member_new_list, name="member_new_list"),
    path('edit/member_list', member_edit_list, name="member_edit_list"),
    path('delete/member_list', member_delete_list, name="member_delete_list"),

    # 実行用ルーティング
    path('member_new', member_new, name="member_new"),
    path('<int:member_id>/edit', member_edit, name="member_edit"),
    path('<int:member_id>/delete', member_delete, name="member_delete"),

]