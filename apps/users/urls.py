from django.urls import path
from .views import register_user, get_users, create_admin

urlpatterns = [
    path('register/', register_user),
    path('all/', get_users),
    path('create-admin/', create_admin),  # ✅ IMPORTANT
]