from django.contrib import messages
from django.core.exceptions import PermissionDenied as Http403, BadRequest as Http400
from django.http import Http404, HttpRequest
from django.shortcuts import render


def handler(request: HttpRequest, exception=None):
    status = 500
    context = {'title': '500 Server Error'}
    if isinstance(exception, Http400):
        status = 400
        context = {'title': '400 Bad Request'}
    elif isinstance(exception, Http403):
        status = 403
        context = {'title': '403 Permission Denied'}
    elif isinstance(exception, Http404):
        status = 404
        context = {'title': '404 Not Found'}

    if request.user.is_staff and exception and getattr(exception, 'args', False):
        for i in exception.args: messages.error(request, i)

    return render(request, '40x.html', context, status=status)


