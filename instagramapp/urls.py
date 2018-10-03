from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.home_images,name='homePage'),
    url(r'^search/', views.search_image, name='search_image'),
    url(r'^image/(\d+)',views.image,name ='image')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)