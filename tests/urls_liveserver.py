from django.conf.urls import patterns, url  # Django >1.4

from django.http import HttpResponse

from .app.models import Item


def _view(request):
    return HttpResponse('Item count: %d' % Item.objects.count())


urlpatterns = patterns(
    '',
    url(r'^item_count/$', _view)
)
