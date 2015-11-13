#
#from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from django.conf.urls import *
from zsz11.view import hello,search,book_id,delete_book
urlpatterns = patterns('',
    ('^hello/$', hello),
    (r'^admin/', include(admin.site.urls)),
    (r'^search/$',search),
    (r'^find_id/$',book_id),
    (r'^delete/$',delete_book),
)
dklrgl
