from django.conf import settings
from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest
from django.utils.module_loading import import_string

from django_summernote.widgets import SummernoteWidget

from .models import Post, Category, Tag, User


widget = getattr(settings, 'DSTORY_WIDGET', None)
if widget: widget = import_string(widget)
else: widget = SummernoteWidget

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': widget(attrs={'style': 'min-width: 70%; max-width: 95%;'}),
        }

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ['user_permissions']

@admin.action(description='공개로 전환')
def make_publish(modeladmin, request, queryset):
    return queryset.update(is_private=False)

@admin.action(description='비공개로 전환')
def make_private(modeladmin, request, queryset):
    return queryset.update(is_private=True)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = [
        'category',
        'is_private',
        'date_pub',
        'password',
        'title',
        'content',
        'tags',
    ] if not getattr(settings, 'DSTORY_SLUG', False) else [
        'category',
        'is_private',
        'date_pub',
        'password',
        'slug',
        'title',
        'content',
        'tags',
    ]
    list_display = [
        'author',
        'title',
        'get_stat',
        'date_pub',
        'category',
        'get_tags',
    ]
    list_display_links = ['title']
    search_fields = ['title', 'text']
    autocomplete_fields = ['tags']
    form = PostForm
    actions = [
        make_publish,
        make_private,
    ]

    @admin.display(description='태그')
    def get_tags(self, obj: Post):
        return ', '.join(map(str, obj.tags.all()))

    @admin.display(description='상태')
    def get_stat(self, obj: Post):
        return '비공개' if obj.is_private else ('비밀' if obj.password else '공개')

    def save_model(self, request: HttpRequest, obj: Post, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = [
        'parent',
        'name',
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']

