from django.urls import path
from .views import register_user, get_users, create_admin, reset_admin_password

urlpatterns = [
    path('', get_users),                         # ✅ GET /api/users/
    path('register/', register_user),            # ✅ POST /api/users/register/
    path('create-admin/', create_admin),         # ✅ GET /api/users/create-admin/
    path('reset-admin-password/', reset_admin_password),  # ✅ GET /api/users/reset-admin-password/
]