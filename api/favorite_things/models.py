from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from django.db import models
from django.contrib.auth import get_user_model


class Favorite(models.Model):
    CATEGORY_CHOICES = [
        ('pe', 'person'),
        ('pl', 'place'),
        ('fo', 'food')
    ]
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=300, null=False)
    ranking = models.IntegerField(null=False, blank=False, unique=True)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    history = AuditlogHistoryField()

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.ranking, self.category)

auditlog.register(Favorite)
