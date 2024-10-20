import json

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import ListView as View
from django.utils import timezone

from .. import settings as dstory_setting
from ..models import Post, Category
from ..forms import SearchForm


order = getattr(settings, 'ORDER', dstory_setting.DSTORY_ORDER)
num_page = getattr(settings, 'DSTORY_PAGE', dstory_setting.DSTORY_PAGE)
# print(f'{num_page=}')
query = {'category__name__in': ['공지사항', '페이지', '서식',]}


class BaseListView(View):
    kwargs: dict
    model = Post
    queryset = Post.objects.filter(is_private=False).exclude(**query)
    paginate_by = num_page
    template_name = 'seolpyo_dstory/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.paginate_by and not self.request.user.is_staff: return queryset.none()
        return self.model.objects.exclude(**query) if self.request.user.is_staff else queryset.filter(date_pub__lte=timezone.now())

    def paginate_queryset(self, *args, **kwargs):
        try: return super().paginate_queryset(*args, **kwargs)
        except:
            self.kwargs['page'] = 1
            return super().paginate_queryset(*args, **kwargs)

    def json_ld(self, object_list: list[Post]):
        url_base = f'{self.request.scheme}://{get_current_site(self.request)}'
        j = {
            '@context': 'http://schema.org',
            '@type': 'BreadcrumbList',
        }
        list_item = []
        for n, i in enumerate(object_list, 1):
            list_item.append({
                '@type': 'ListItem',
                'position': n,
                'item': {
                    '@id': url_base + i.get_absolute_url(),
                    'name': f'{i}',
                }
            })
        j['itemListElement'] = list_item

        return json.dumps(j, ensure_ascii=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context['page_obj'].number if context['page_obj'] else 1
        context.update({
            'page': page,
            'canonical': f'{self.request.path_info}?page={page}',
            'json_ld': self.json_ld(context['object_list']),
        })
        return context


class ListView(BaseListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = '전체 글 목록'
        context.update({
            'title': title,
            'notice_list': Post.objects.filter(is_private=False, category__name='공지사항'),
            'description': f"{title} {context['page']:,}페이지",
        })
        return context


class SearchView(BaseListView):
    queryset = Post.objects.filter(is_private=False)
    def get_queryset(self):
        form = SearchForm(data=self.kwargs)
        if form.is_valid():
            if self.request.user.is_staff: self.queryset = self.model.objects.all()
            queryset = None
            for i in form.cleaned_data['keyword'].split():
                if not queryset:
                    queryset = self.queryset.filter(title__icontains=i)
                    queryset |= self.queryset.filter(text__icontains=i)
                else:
                    queryset |= self.queryset.filter(title__icontains=i)
                    queryset |= self.queryset.filter(text__icontains=i)
            return queryset.distinct().order_by(*order)
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.kwargs.get('keyword', '')
        context.update({
            'title': f"'{title}' 검색 결과",
            'description': f"{title} {context['page']:,}페이지",
        })
        return context


class CategoryListView(BaseListView):
    def get_queryset(self):
        self.category = Category.objects.get(name=self.kwargs['category'])
        if not self.kwargs.get('category_parent'): queryset = self.queryset.filter(category=self.category)
        else:
            queryset = self.queryset.filter(
                category__parent__name=self.kwargs['category_parent'],
                category__name=self.kwargs['category']
            )
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.category
        context.update({
            'title': f"'{title}' 글 목록",
            'description': f"{title} {context['page']:,}페이지",
        })
        return context


class TagListView(BaseListView):
    def get_queryset(self):
        queryset = self.queryset.filter(tags__name=self.kwargs['tag'])
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.kwargs['tag']
        context.update({
            'title': f"#{title}",
            'description': f"{title} {context['page']:,}페이지",
        })
        return context


class NoticeListView(BaseListView):
    model = Post
    queryset = Post.objects.filter(category__name='공지사항',)
    def get_queryset(self):
        queryset = self.model.objects.filter(category__name='공지사항',)
        if not self.request.user.is_staff: queryset = queryset.exclude(is_private=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = '공지사항'
        context.update({
            'title': title,
            'description': f"{title} {context['page']:,}페이지",
        })
        return context


class PageListView(BaseListView):
    queryset = Post.objects.filter(is_private=False, category__name='페이지',)

