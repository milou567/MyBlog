from django.contrib import admin
from django.utils.safestring import mark_safe

from user_profile.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'phone', 'bith_date', "get_image")
    search_fields = ('country',)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="50" height="60"')

    get_image.short_description = "Аватар"