from django.urls import path
from .views import register_user, get_users, create_admin, reset_admin_password

urlpatterns = [
    path('register/', register_user),
    path('all/', get_users),
    path('create-admin/', create_admin),
    path('reset-admin-password/', reset_admin_password),  # ✅ IMPORTANT
]