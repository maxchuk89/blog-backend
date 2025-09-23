# sensive_blog/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# 👇 эти два импорта нужны для /favicon.ico
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path(
        'favicon.ico',
        RedirectView.as_view(url=staticfiles_storage.url('img/favicon.png'), permanent=True),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
