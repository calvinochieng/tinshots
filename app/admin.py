from django.contrib import admin
from .models import Portfolio, PortfolioImage, ContactMessage, Booking


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')
    search_fields = ('name', 'email', 'phone')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('shoot_type','full_name', 'email', 'phone', 'date', 'time', 'created_at')
    search_fields = ('name', 'email', 'phone')

class PortfolioImageInline(admin.TabularInline):  # Or use admin.StackedInline for a vertical layout
    model = PortfolioImage
    extra = 3  # Number of extra blank fields to display for adding new images
    fields = ('image',)  # Only display the image field


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'order')  # Fields to display in the admin list view
    inlines = [PortfolioImageInline]  # Add the inline model to the Portfolio admin
    search_fields = ('title',)  # Search bar for the title field
    ordering = ('order',)  # Order portfolios alphabetically
