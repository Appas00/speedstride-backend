from django.urls import path
from .views import register_user, get_users, create_admin

urlpatterns = [
    path('register/', register_user),
    path('all/', get_users),                 # ✅ better than empty path
    path('create-admin/', create_admin),     # ✅ THIS IS MISSING NOW
]