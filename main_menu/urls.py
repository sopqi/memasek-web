from django.urls import path, re_path  # Добавили re_path
from . import views
from django.conf import settings
from django.views.static import serve  # Добавили импорт serve

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('<int:mem_id>/', views.mem_view, name='mem_detail'),
    path('user/<slug:username>/', views.profile, name='profile'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('like/<int:mem_id>/', views.like_mem, name='like_mem'),
    path('delete/<int:mem_id>/', views.delete_mem, name='delete_mem'),

    # Принудительная раздача медиа-файлов (картинок) при выключенном DEBUG:
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]