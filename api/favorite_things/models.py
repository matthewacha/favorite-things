from django.db import models
from django.contrib.auth import get_user_model


class Favorite(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False)
    ranking = models.IntegerField(null=False, blank=False)
    category =  models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    audit_log = models.CharField(max_length=350, null=False, blank=False)

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.ranking, self.category)
