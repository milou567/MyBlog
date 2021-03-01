from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from articles.models import Article
from articles.models import Rating
from articles.models import RatingStar
from articles.models import Review


class ArticleAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""

    content = forms.CharField(label="Текст статьи", widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = "__all__"


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
    actions = ["publish", "unpublish"]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    form = ArticleAdminForm
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.art_image.url} width="50" height="60"')

    get_image.short_description = "Изображение"

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ("change",)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ("change",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "article", "id")
    readonly_fields = ("name", "email")


admin.site.site_title = "MyBlog"
admin.site.site_header = "MyBlog"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""

    list_display = ("star", "article", "ip")


admin.site.register(RatingStar)
