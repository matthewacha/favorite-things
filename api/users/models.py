from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=150, null=False,
                            blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.name)


auditlog.register(CustomUser)
