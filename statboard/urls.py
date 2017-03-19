from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from statboard.core.views import index, metric_view

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
]

for metric in settings.METRICS:
    urlpatterns.append(url(r'^metric/%s$' % metric, metric_view, name=metric))
