from django.contrib import admin
from django.urls import path, include
from main_menu.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_menu.urls')),
    path('account/signup', SignUpView.as_view(), name='signup'),
    path('account/', include('django.contrib.auth.urls')),
]

