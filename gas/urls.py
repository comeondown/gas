from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from main.views import *
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
     url(r'^catalog/([0-9]+)/([0-9]+)', product, name='product'),
    url(r'^catalog/([0-9]+)', product_list, name='product_list'),
    url(r'^catalog/', catalog, name='catalog'),
	url(r'^$', index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
