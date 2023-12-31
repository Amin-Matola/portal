from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from core import models

# The Restraunts Model
from apps.restraunts import models as restrant_models

admin.site.register(models.SupportedLanguage)
admin.site.register(models.ApplicationSetting)
admin.site.register(models.Tenant)
admin.site.register(models.Address)
admin.site.register(models.TenantUser)
admin.site.register(restrant_models.Restraunt)
