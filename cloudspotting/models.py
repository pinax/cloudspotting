from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from pinax.images.models import ImageSet


@python_2_unicode_compatible  # needed to support Python 2
class CloudSpotting(models.Model):
    """
    A collection of images of a particular cloud type.
    """
    cloud_type = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="+")
    image_set = models.ForeignKey(ImageSet, blank=True, null=True)

    class Meta:
        unique_together = ("cloud_type", "user")

    def get_absolute_url(self):
        return reverse("cloudspotting_detail", kwargs=({"pk": self.pk}))

    def __str__(self):
        return "{} - {}".format(self.user, self.cloud_type)
