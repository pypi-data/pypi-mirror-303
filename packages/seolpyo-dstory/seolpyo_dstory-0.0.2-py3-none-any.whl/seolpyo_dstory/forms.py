from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.module_loading import import_string

from django_summernote.widgets import SummernoteWidget

from .models import Post, Tag


widget = getattr(settings, 'DSTORY_WIDGET', None)
if widget: widget = import_string(widget)
else: widget = SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'category',
            'is_private',
            'date_pub',
            'password',
            'slug',
            'title',
            'content',
            'tags',
        ]
        widgets = {
            # 'password': forms.PasswordInput(render_value=True),
            'date_pub': forms.DateTimeInput(attrs={'type': 'datetime-local', 'max': timezone.now() + timezone.timedelta(days=365),}),
            'content': widget(),
        }

    tags = forms.CharField(
        label='태그',
        required=False,
        widget=forms.SelectMultiple(
            choices=[],
            attrs={
                'class': 'js-example-basic-multiple js-states form-control',
                'multiple': 'multiple',
            }
        ),
    )

    def clean_tags(self):
        list_tag = []
        data = self.cleaned_data['tags']
        if data:
            data = eval(data)
            for i in data:
                tag, _ = Tag.objects.get_or_create(name=i)
                list_tag.append(tag.pk)
        return list_tag

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget.choices = [(i, i) for i in Tag.objects.all()]
        if not getattr(settings, 'DSTORY_SLUG', False): del self.fields['slug']


class PasswordForm(forms.Form):
    password = forms.CharField(
        label='조회 비밀번호',
        widget=forms.PasswordInput(render_value=True)
    )


class SearchForm(forms.Form):
    keyword = forms.CharField(
        max_length=20,
        min_length=1,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control me-2',
                'placeholder': '검색어를 입력하세요.',
                'type': 'search',
                'aria-label': 'Search',
            }
        ),
    )
    
    def clean_keyword(self):
        data: str = self.cleaned_data['keyword']
        if not ''.join(data.split()):
            raise ValidationError()
        return data
