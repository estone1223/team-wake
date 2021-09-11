from wakes.views import wake_new, wake_detail, wake_edit, wake_classic, wake_delete
from django.urls import path




urlpatterns = [
    # wake関係
    path('new/', wake_new, name='wake_new'),
    path('<int:wake_id>/', wake_detail, name='wake_detail'),
    path('<int:wake_id>/delete/', wake_delete, name='wake_delete'),
    path('<int:wake_id>/edit/', wake_edit, name='wake_edit'),

    # 簡易版ルーティング
    path('classic/', wake_classic, name='wake_classic'),

]