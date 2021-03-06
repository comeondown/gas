from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from main.views import *
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^sjsadminpanel/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^product/([0-9]+)', product, name='product'),
    url(r'^catalog/([0-9]+)', product_list, name='product_list'),
    url(r'^catalog/', catalog, name='catalog'),
    url(r'^addspecification/([0-9]+)', addSpecification, name='add_specification'),
    url(r'^about/', about, name='about'),
	url(r'^$', index, name='index'),
]

#if settings.DEBUG:
#	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#	urlpatterns += staticfiles_urlpatterns()
