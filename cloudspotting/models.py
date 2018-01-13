from django.conf import settings
from django.urls import reverse
from django.db import models

from pinax.images.models import ImageSet


class CloudSpotting(models.Model):
    """
    A collection of images of a particular cloud type.
    """
    cloud_type = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="+", on_delete=models.CASCADE)
    image_set = models.OneToOneField(ImageSet, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("cloud_type", "user")
        ordering = ["user", "cloud_type"]

    def get_absolute_url(self):
        return reverse("cloudspotting_detail", kwargs=({"pk": self.pk}))

    def __str__(self):
        return "{} - {}".format(self.user, self.cloud_type)
