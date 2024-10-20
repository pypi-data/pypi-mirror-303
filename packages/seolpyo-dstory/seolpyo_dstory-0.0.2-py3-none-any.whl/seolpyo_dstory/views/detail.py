import json

from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404
from django.http import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView as View
from django.utils import timezone

from .. import settings as dstory_setting
from ..models import Post
from ..forms import PasswordForm


order = getattr(settings, 'DSTORY_ORDER', dstory_setting.DSTORY_ORDER)


class BaseView(View):
    template_name = 'seolpyo_dstory/detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset if self.request.user.is_staff else queryset.filter(date_pub__lte=timezone.now())

    def get_object(self, queryset=None):
        obj: Post = super().get_object(queryset)
        if obj.is_private and not self.request.user.is_staff:
            raise Http404
        return obj

    def json_ld(self):
        url_base = f'{self.request.scheme}://{get_current_site(self.request)}'
        description = self.object.description
        if 500 < len(description): description = description[:498] + '..'
        j = {
            '@context': 'http://schema.org',
            '@type': 'BlogPosting',
            'mainEntityOfPage': url_base + self.object.get_absolute_url(),
            'url': url_base + self.object.get_absolute_url(),
            'headline': f'{self.object}',
            'description': description,
            'author': {
                '@type': 'Person',
                'name': f'{self.object.author}',
            },
            'datePublished': f'{self.object.date_pub}',
        }
        if self.object.thumbnail:
            j['image'] = {
                '@type': 'ImageObject',
                'url': self.object.thumbnail,
            }

        return json.dumps(j, ensure_ascii=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context.update({
            'form': PasswordForm(data=(self.request.POST if self.request.method == 'POST' else None)),
            'canonical': self.object.get_absolute_url(),
            'description': self.object.description if len(self.object.description) < 121 else f'{self.object.description[:118]}..',
            'object_list': queryset.filter(category=self.object.category, is_private=False).order_by(*order) if self.object.category else [],
            'json_ld': self.json_ld(),
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        if not self.object.password or self.object.author == self.request.user or self.request.user.is_staff:
            r = super().render_to_response(context, **response_kwargs)
        else:
            messages.info(self.request, '조회 비밀번호를 입력해주세요.')
            r = render(self.request, 'seolpyo_dstory/form.html', context, status=401)
        return r

    def form_valid(self, context): return super().render_to_response(context)

    def form_invalid(self, context):
        messages.error(self.request, '조회 비밀번호가 일치하지 않습니다.', 'danger')
        return render(self.request, 'seolpyo_dstory/form.html', context, status=401)

    def post(self, request, *arg, **kwargs):
        self.object: Post = self.get_object()
        context = self.get_context_data()
        form: PasswordForm = context['form']
        if form.is_valid() and self.object.password == form.cleaned_data['password']:
            return self.form_valid(context)
        return self.form_invalid(context)


class DetailView(BaseView):
    queryset = Post.objects.exclude(category__name__in=['공지사항', '페이지', '서식',])

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        if not slug: obj = super().get_object(queryset)
        else:
            try: obj = self.queryset.get(slug=slug)
            except self.model.DoesNotExist: obj = self.queryset.get(slug_title=slug)
        if obj.is_private and not self.request.user.is_staff:
            raise Http404
        return obj


class NoticeView(BaseView):
    queryset = Post.objects.filter(category__name='공지사항',)


class PageView(View):
    queryset = Post.objects.filter(category__name='페이지',)

