from django.db import models
from n2_utils.base.models import BaseModel

class EBillIntegration(BaseModel):
    app_name = models.CharField(max_length=256)
    url = models.CharField(max_length=256, verbose_name="Base Url")
    smmm_turmob_key = models.CharField(max_length=256, blank=True, null=True)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    sync = models.BooleanField(default=False)

   