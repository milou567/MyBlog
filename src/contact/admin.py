from django.contrib import admin

from .models import Newsletter, AddOrder


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "date")


@admin.register(AddOrder)
class AddOrderAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "website", "country", "text")
