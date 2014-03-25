from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'el.views.home', ),
    url(r'^link1$', 'el.views.link1', ),
    url(r'^link2$', 'el.views.link2', ),
    url(r'^link3$', 'el.views.link3', ),
    url(r'^link4$', 'el.views.link4', ),
    url(r'^home$', 'el.views.link5', ),
)
