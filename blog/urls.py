from django.urls import path, include, re_path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('post_detail/<int:id>',views.post_detail,name='post_detail'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

#if settings.DEBUG:
#    urlpatterns


#path('ckeditor/', include('ckeditor_uploader.urls')),
