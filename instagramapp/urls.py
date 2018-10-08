from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.home_images,name='homePage'),
    url(r'^search/', views.search_users, name='search_users'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^users/', views.user_list, name = 'user_list'),
    url(r'^new/image$', views.new_image, name='new_image'),
    url(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    url(r'^profile/(?P<username>[0-9]+)$', views.individual_profile_page, name='individual_profile_page'),
    # url(r'^comment/(?P<image_id>\d+)', views.add_review, name='add_review'),
    url(r'^myprofile/$', views.myprofile, name='myprofile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)