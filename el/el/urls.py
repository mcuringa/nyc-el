from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'el.views.home', ),
    url(r'^home$', 'el.views.home', ),
    url(r'^cityForm$', 'el.views.cityFormFill', ),
    url(r'^save_train$', 'el.views.save_train', ),
	url(r'^cities/([0-9]?)[/]$', 'el.views.infoDisplayer'),
	url(r'^(?P<pk>[0-9]+?)/view[/]$', 'el.views.infoDisplayer', ),
	url(r'^(?P<pk>[0-9]+?)/cities[/]$', 'el.views.infoDisplayer', ),
	url(r'^search$', 'el.views.search', ),

)
