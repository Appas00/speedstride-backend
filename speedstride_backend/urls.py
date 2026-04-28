from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

# ✅ Redirect to frontend (GitHub Pages)
def home(request):
    return redirect("https://appas00.github.io/speedstride-frontend/")

urlpatterns = [
    # ✅ Home → opens frontend
    path('', home),

    # ✅ Admin panel
    path('admin/', admin.site.urls),

    # ✅ API routes
    path('api/products/', include('apps.products.urls')),
    path('api/orders/', include('apps.orders.urls')),
    path('api/users/', include('apps.users.urls')),
]

# ✅ Serve media files (for product images)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)