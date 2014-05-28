from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.hello', name='hello'),
    url(r'^hi/$', 'app.views.say_hi', name='hi'),
    url(r'^blog/$', 'app.views.blog'),
    url(r'^blog/submit/$', 'app.views.submit_post'),
)
