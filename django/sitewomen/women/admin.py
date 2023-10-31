from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from women.models import Women, Category, TagPosts, Husband


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'photo', 'post_photo', ('cat', 'husband'), 'tags')
    filter_horizontal = ('tags',)
    list_display = ('title', 'post_photo', 'time_create', 'cat', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = (MarriedFilter, 'is_published', 'cat__name')
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 7
    actions = ['set_published', 'set_draft']
    save_on_top = True
    readonly_fields = ['post_photo' ]
    # exclude =


    @admin.display(description='Изображение', ordering='content')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50>")


    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
            count = queryset.update(is_published=Women.Status.PUBLISHED)
            self.message_user(request, f'Изменено {count} записей.')

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'{count} записей снято с публикации.', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')


@admin.register(TagPosts)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'slug')


@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')


