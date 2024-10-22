from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    created_user = models.ForeignKey('user.User', on_delete=models.RESTRICT, related_name='created_by_%(app_label)s_%(class)s_related', blank=True, null=True)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='company_%(app_label)s_%(class)s_related', blank=True, null=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def hard_delete(self, *args, **kwargs):
        pass
