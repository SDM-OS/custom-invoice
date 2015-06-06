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

class ServiceResource(ModelResource):
    class Meta:
        queryset = Service.objects.all()
        resource_name = 'service'
        allowed_methods = ['post', 'get']


class JobResource(ModelResource):
    attender = fields.ForeignKey('main.api.AttenderResource', 'attender', null=True)
    service_type = fields.ForeignKey('main.api.ServiceResource', 'service_type', null=True)

    class Meta:
        queryset = Job.objects.all()
        resource_name = 'job'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        always_return_data = True