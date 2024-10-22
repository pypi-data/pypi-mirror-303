from django.db import models
from n2_utils.base.models import BaseModel

class Application(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Uygulama Adı")
    key = models.CharField(max_length=256, verbose_name="Uygulama Keyi")
    url = models.CharField(max_length=256, verbose_name="Uygulama Domaini")
    dev_url = models.CharField(max_length=256, null=True, verbose_name="Uygulama Development Ortam Domaini")
    icon = models.CharField(max_length=256, null=True, blank=True, verbose_name="Uygulama İkonu")
    color = models.CharField(max_length=256, null=True, blank=True, verbose_name="İkon Rengi")
    description = models.TextField(null=True, blank=True, verbose_name="Açıklama")
    image = models.ImageField(null=True, blank=True, verbose_name="Örnek Resim")

    class Meta:
        managed = False
        db_table = 'core"."application'
