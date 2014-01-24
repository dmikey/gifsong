from django.conf.urls import patterns, include, url

from gifsong.views import addgifsong, showgifsong

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gifsong.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')) 
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addgifsong/', addgifsong.as_view(), name='AddGifSong'),
    url(r'^show/', showgifsong.as_view(), name='ShowGifSong'),
    url(r'^$', addgifsong.as_view(), name='home'),
)
