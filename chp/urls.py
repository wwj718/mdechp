from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView, RedirectView
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^$', RedirectView.as_view(url='/home/')),
    url(r'^home/', include('home.urls')),
    url(r'^wwj/', include("wwj.urls")),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
