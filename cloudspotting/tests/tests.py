from django.core.urlresolvers import reverse

from pinax.images.models import ImageSet

from ..models import CloudSpotting
from .test import TestCase


class TestViews(TestCase):

    def setUp(self):
        super(TestViews, self).setUp()
        self.user = self.make_user("cirrus")
        self.cloud_type = "cumulonimbus"
        self.spotting = CloudSpotting.objects.create(
            cloud_type=self.cloud_type,
            user=self.user,
            image_set=ImageSet.objects.create(created_by=self.user)
        )

    def test_list(self):
        """
        Ensure list contains all CloudSpotting collections.
        """
        path = reverse("cloudspotting_list")
        with self.login(self.user):
            self.get(path)
            self.response_200()
            object_list = self.get_context("object_list")
            self.assertEqual(object_list[0], self.spotting)

    def test_invalid_detail(self):
        """
        Ensure GET with invalid CloudSpotting PK fails.
        """
        with self.login(self.user):
            self.get("cloudspotting_detail", pk=555)
            self.response_404()

    def test_detail(self):
        """
        Ensure GET with valid CloudSpotting PK succeeds.
        """
        with self.login(self.user):
            self.get("cloudspotting_detail", pk=self.spotting.pk)
            self.response_200()
            context_object = self.get_context("cloudspotting")
            self.assertEqual(context_object, self.spotting)

    def test_create(self):
        """
        Ensure successful CloudSpotting creation.
        """
        cloud_type = "nimbus"
        post_args = dict(
            cloud_type=cloud_type
        )
        with self.login(self.user):
            self.post("cloudspotting_create", data=post_args, follow=True)
            self.response_200()
            self.assertTrue(
                next(iter(CloudSpotting.objects.filter(cloud_type=cloud_type)), None)
            )

    def test_delete(self):
        """
        Ensure CloudSpotting is really deleted.
        """
        with self.login(self.user):
            self.post("cloudspotting_delete", pk=self.spotting.pk, follow=True)
            self.response_200()
            self.assertFalse(
                next(iter(CloudSpotting.objects.filter(cloud_type=self.spotting.cloud_type)), None)
            )
