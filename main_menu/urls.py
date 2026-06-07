from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('<int:mem_id>/', views.mem_view, name='mem_detail'),
    path('user/<slug:username>/', views.profile, name='profile'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('like/<int:mem_id>/', views.like_mem, name='like_mem'),
    path('delete/<int:mem_id>/', views.delete_mem, name='delete_mem'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)