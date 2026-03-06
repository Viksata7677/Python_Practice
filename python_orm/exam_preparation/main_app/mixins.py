from django.db import models


class AwardedMixin(models.Model):
    is_awarded = models.BooleanField(default=False)

    class Meta:
        abstract = True