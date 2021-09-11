from wakes.views import top
from django.contrib import admin
from django.urls import path
from django.urls.conf import include



urlpatterns = [
    path('', top, name='top'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('wakes/', include('wakes.urls')),
    # member関係
    path('member/', include('member.urls')),
]