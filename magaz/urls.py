from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^order/', include('orders.urls', namespace='orders')),
    url(r'^cupons/', include('cupons.urls', namespace='cupon')),
    url(r'^', include('blog.urls', namespace='blog')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
