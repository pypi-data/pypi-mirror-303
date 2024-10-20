import json

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest
from django.shortcuts import resolve_url
from django.utils.module_loading import import_string

from .models import Category, Tag
from .forms import SearchForm
from . import settings as default_setting


form_search = getattr(settings, 'DSTORY_FORM_SEARCH', None)
if form_search: form_search = import_string(form_search)
else: form_search = SearchForm

default_context = default_setting.DSTORY_CONTEXT
default_context.update({
    'category_list': Category.objects.filter(parent=None).exclude(name__in=['서식', '페이지',]),
    'tag_list': Tag.objects.all(),
})


def get_context(request: HttpRequest):
    url_base = f'{request.scheme}://{get_current_site(request)}'
    context = default_context
    context.update(getattr(settings, 'DSTORY_CONTEXT', {}))

    is_tistory_user = settings.AUTH_USER_MODEL == 'seolpyo_dstory.User'

    name_login = getattr(settings, 'DSTORY_LOGIN_NAME', default_setting.DSTORY_LOGIN_NAME if is_tistory_user else None)
    try: url_login = resolve_url(name_login) if name_login else None
    except: url_login = None

    name_logout = getattr(settings, 'DSTORY_LOGOUT_NAME', default_setting.DSTORY_LOGOUT_NAME if is_tistory_user else None)
    try: url_logout = resolve_url(name_logout) if name_logout else None
    except: url_logout = None

    favicon = getattr(settings, 'DSTORY_FAVICON', '')
    if favicon and favicon.startswith('/'): favicon = f'//{url_base}{favicon}'

    lightbox = default_setting.DSOTRY_LIGHTBOX
    lightbox.update(getattr(settings, 'DSOTRY_LIGHTBOX', {}))

    context.update({
        'form_search': form_search(initial=request.resolver_match.kwargs),
        'url_login': url_login, 'url_logout': url_logout,
        'url_base': url_base,
        'favicon': favicon,
        'lightbox': json.dumps(lightbox),
    })
    return context

