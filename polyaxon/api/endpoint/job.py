from rest_framework.generics import get_object_or_404

import access

from api.endpoint.project import ProjectPermission, ProjectResourceEndpoint
from db.models.jobs import Job


class JobEndpoint(ProjectResourceEndpoint):
    queryset = Job.objects
    CONTEXT_KEYS = ProjectResourceEndpoint.CONTEXT_KEYS + ('job_id',)
    CONTEXT_OBJECTS = ProjectResourceEndpoint.CONTEXT_OBJECTS + ('job',)
    lookup_url_kwarg = 'job_id'

    def _initialize_context(self):
        #  pylint:disable=attribute-defined-outside-init
        super()._initialize_context()
        self.job = self.get_object()


class JobResourceListEndpoint(ProjectResourceEndpoint):
    CONTEXT_KEYS = ProjectResourceEndpoint.CONTEXT_KEYS + ('job_id',)
    CONTEXT_OBJECTS = ProjectResourceEndpoint.CONTEXT_OBJECTS + ('job',)
    lookup_url_kwarg = 'job'

    def enrich_queryset(self, queryset):
        return queryset.filter(job=self.job)

    def _initialize_context(self):
        #  pylint:disable=attribute-defined-outside-init
        super()._initialize_context()
        self.job = get_object_or_404(Job,
                                     id=self.job_id,
                                     project=self.project)


class JobResourcePermission(ProjectPermission):
    SCOPE_MAPPING = access.get_scope_mapping_for('ProjectResource')

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj.job.project)


class JobResourceEndpoint(JobResourceListEndpoint):
    permission_classes = (JobResourcePermission,)
    AUDITOR_EVENT_TYPES = None
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
