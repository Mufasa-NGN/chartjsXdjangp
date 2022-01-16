from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'figure', 'bio')
    list_display_links = ('name', )
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Profile, ProfileAdmin)

