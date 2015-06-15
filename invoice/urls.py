from django.conf.urls import patterns, include, url
from django.contrib import admin

from main.views import AddjobView

from main.api import JobResource, ServiceResource, AttenderResource
from tastypie.api import Api
import main.api

api = Api(api_name='v1')
api.register(main.api.JobResource())
api.register(main.api.ServiceResource())
api.register(main.api.AttenderResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    # url(r'^dashboard/', 'main.views.dashboard', name='dashboard'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^dashboard/add/', AddjobView.as_view()),
    url(r'^api/', include(api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
