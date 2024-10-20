from django.conf import settings
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from django.views.generic import CreateView, UpdateView, DeleteView as DV
from django.shortcuts import resolve_url
from django.utils.module_loading import import_string

from ..models import Post, Category
from ..forms import PostForm


class BasePost:
    model = Post
    request: HttpRequest
    form_class = PostForm
    template_name = 'seolpyo_dstory/summernote.html'

    def get_from_class(self):
        form = getattr(settings, 'DSTORY_FORM', None)
        if form: form = import_string(form)
        else: form = self.form_class
        if not self.request.user.is_staff:
            category = Category.objects.exclude(name__in=['공지사항', '페이지', '서식',])
            form.fields['category'].queryset = category
        return form

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff: raise PermissionDenied
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_staff: raise PermissionDenied
        return super().post(request, *args, **kwargs)


class PostView(BasePost, CreateView):
    extra_context = {'title': '글 작성'}

    def form_valid(self, form):
        setattr(form.instance, 'author', self.request.user)
        return super().form_valid(form)


class EditView(BasePost, UpdateView):
    extra_context = {'title': '글 수정'}


class DeleteView(DV):
    model = Post

    def get_object(self, queryset=None):
        obj: Post = super().get_object(queryset)
        if obj.author != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied
        return obj

    def get_success_url(self):
        messages.success(self.request, '글을 삭제했습니다.')
        return resolve_url('seolpyo_dstory:list')


