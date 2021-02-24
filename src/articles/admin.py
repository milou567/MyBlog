from django.contrib import admin
from django.utils.safestring import mark_safe

from articles.models import Article
from articles.models import Review


class ReviewInline(admin.TabularInline):
    """Отзывы на странице публикации"""

    model = Review
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author", "draft", "get_image")
    search_fields = ("title",)
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.art_image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "article", "id")
    readonly_fields = ("name", "email")


admin.site.site_title = "MyBlog"
admin.site.site_header = "MyBlog"
