from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'el.views.home', ),
    url(r'^link1$', 'el.views.link1', ),
    url(r'^hongkong$', 'el.views.hongkong', ),
    url(r'^tokyo$', 'el.views.tokyo', ),
    url(r'^cityForm$', 'el.views.cityForm', ),
    url(r'^mexico$', 'el.views.mexico', )
    url(r'^home$', 'el.views.link5', ),

)
