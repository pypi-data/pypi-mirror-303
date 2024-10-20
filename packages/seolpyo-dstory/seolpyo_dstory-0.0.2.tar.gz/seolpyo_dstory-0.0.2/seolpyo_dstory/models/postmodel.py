from re import findall

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import resolve_url
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.sites.models import Site

from bs4 import BeautifulSoup


def default_category():
    for i in ['공지사항', '페이지', '서식',]: Category.objects.get_or_create(name=i)
    return


class BaseCategory(models.Model):
    class Meta:
        abstract = True
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리'

    name = models.CharField(
        verbose_name='카테고리명',
        unique=True,
        max_length=10,
        default=default_category,
    )

class CategoryManager(models.Manager):
    def get_queryset(self): return super().get_queryset().prefetch_related('dstory_category_children')

class Category(BaseCategory):
    objects = CategoryManager()

    parent: BaseCategory = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='dstory_category_children',
        null=True,
    )

    def __str__(self):
        if self.parent: return f'{self.parent}/{self.name}'
        return self.name

    def get_absolute_url(self):
        if self.name == '공지사항': return resolve_url('seolpyo_dstory:list_notice')
        if self.name == '페이지': return '#'
        if self.parent: return resolve_url('seolpyo_dstory:category', self.parent.name, self.name)
        return resolve_url('seolpyo_dstory:category', self.name)

    def clean(self):
        if self.parent and (self.parent.parent or self.parent.name in {'공지사항', '페이지', '서식'}):
            raise ValidationError({'parent': '하위 카테고리를 가질 수 없는 카테고리입니다.'})
        return super().clean()


class BaseTag(models.Model):
    class Meta:
        abstract = True
        verbose_name = '태그'
        verbose_name_plural = '태그'

    name = models.CharField(
        verbose_name='태그명',
        unique=True,
        max_length=19,
    )

    def __str__(self): return self.name

    def get_absolute_url(self): return resolve_url('seolpyo_dstory:tag', self.name)

class Tag(BaseTag):
    pass


class BasePost(models.Model):
    class Meta:
        abstract = True
        verbose_name = '티스토리/글'
        verbose_name_plural = '글'
        ordering = ['-date_pub', '-pk']

    date_pub = models.DateTimeField(
        verbose_name='공개시간',
        default=timezone.localtime,
    )

    slug = models.CharField(
        verbose_name='문자 주소',
        max_length=99,
        unique=True,
        null=True,
    )

    password = models.CharField(
        verbose_name='비밀번호',
        max_length=20,
        blank=True,
    )

    is_private = models.BooleanField(
        verbose_name='비공개로 설정',
        default=False,
    )

    title = models.CharField(
        verbose_name='제목',
        max_length=99,
    )

    slug_title = models.SlugField(
        verbose_name='문자 주소(자동생성)',
        unique=True,
        editable=False,
        allow_unicode=True,
    )

    content = models.TextField(
        verbose_name='내용',
        # max_length=99999,
    )

    text = models.TextField(editable=False,)

    _description = None
    @property
    def description(self):
        if not self._description: self._description = self.text if len(self.text) < 501 else f'{self.text[:498]}..'
        return self._description
    
    _thumbnail = None
    @property
    def thumbnail(self):
        if self._thumbnail is None:
            soup = BeautifulSoup(self.content, 'html.parser')
            img = soup.select_one('img')
            if img:
                self._thumbnail = img['src']
                if self._thumbnail.startswith('/'): self._thumbnail = f"//{Site.objects.get_current().domain if not settings.DEBUG else '127.0.0.1:8000'}{self._thumbnail}"
            else: self._thumbnail = False

        return self._thumbnail

    def __str__(self): return self.title

class PostManager(models.Manager):
    def get_queryset(self): return super().get_queryset().prefetch_related('author', 'category', 'tags')

class Post(BasePost):
    objects = PostManager()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='seolpyo_dstory_post_set',
        verbose_name='작성자',
        editable=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='seolpyo_dstory_post_set',
        verbose_name='카테고리',
        blank=True,
        null=True,
        default=default_category,
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='seolpyo_dstory_post_set',
        verbose_name='태그',
        blank=True,
    )

    def get_absolute_url(self):
        if self.category:
            if self.category.name == '공지사항': return resolve_url('seolpyo_dstory:notice', self.pk)
            if self.category.name == '페이지': return resolve_url('seolpyo_dstory:page', self.pk)
            if self.category.name == '서식': return resolve_url('seolpyo_dstory:template', self.pk)
        if getattr(settings, 'DSTORY_SLUG', False): return resolve_url('seolpyo_dstory:detail_slug', self.slug if self.slug else self.slug_title)
        return resolve_url('seolpyo_dstory:detail', self.pk)

    def set_slug_title(self):
        slug = slugify(self.title, allow_unicode=True)
        queryset = self.__class__.objects.filter(slug_title__contains=slug)
        if self.pk: queryset = queryset.exclude(pk=self.pk)
        list_slug = queryset.values_list('slug_title', flat=True)

        list_re = []
        for s in list_slug:
            i = findall(f'^{slug}\-([0-9]+)$', ' '.join(s))
            if i: list_re += i
        if list_re:
            mn = max(map(int, list_re))
            slug = f'{slug}-{mn+1}'
        self.slug_title = slug
        return

    def save(self, *args, **kwargs):
        self.set_slug_title()
        self.text = ' '.join(BeautifulSoup(self.content, 'html.parser').text.split())

        if self.category and self.category.name == '서식': self.is_private = True

        return super().save(*args, **kwargs)
