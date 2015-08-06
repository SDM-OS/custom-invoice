from tastypie.resources import ModelResource
from tastypie import http, fields
from tastypie.utils import trailing_slash
from tastypie.exceptions import Unauthorized, ImmediateHttpResponse

from main.models import Job, Attender, Service


class AttenderResource(ModelResource):
    class Meta:
        queryset = Attender.objects.all()
        resource_name = 'attender'
        allowed_methods = ['post', 'get']


class JobResource(ModelResource):
    attender = fields.ForeignKey('main.api.AttenderResource', 'attender', null=True)

    class Meta:
        queryset = Job.objects.all()
        resource_name = 'job'
        detail_allowed_methods = ['put', 'post']
        list_allowed_methods = ['get', 'post']
        always_return_data = True