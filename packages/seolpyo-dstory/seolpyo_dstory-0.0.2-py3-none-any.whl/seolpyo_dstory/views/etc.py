from django.conf import settings
from django.http import Http404, HttpResponse


def naver(request, code):
    txt = getattr(settings, 'DSTORY_NAVER', False)
    if not txt or code != txt: raise Http404
    return HttpResponse(content=f'naver-site-verification: naver{code}.html', content_type='text/plain')


def robots(request):
    txt = getattr(settings, 'DSTORY_ROBOTS', False)
    if not txt: raise Http404
    return HttpResponse(content=txt, content_type='text/plain')


def adsense(request):
    txt = getattr(settings, 'DSTORY_CONTEXT', {}).get('adsense', None)
    if not txt: raise Http404
    return HttpResponse(content=f'google.com, pub-{txt}, DIRECT, f08c47fec0942fa0', content_type='text/plain')

