from django.contrib import admin
from .models import Order

# ✅ Change Django Admin Titles
admin.site.site_header = "SpeedStride Administration"
admin.site.site_title = "SpeedStride Admin"
admin.site.index_title = "Welcome to SpeedStride Dashboard"


# ✅ Register Order Model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    # Table view
    list_display = (
        'name',
        'email',
        'phone',
        'product_name',
        'quantity',
        'total_price',
        'created_at'
    )

    # Filters (right side)
    list_filter = ('created_at',)

    # Search
    search_fields = ('name', 'email', 'product_name')

    # Latest first
    ordering = ('-created_at',)

    # Read-only fields
    readonly_fields = ('created_at',)