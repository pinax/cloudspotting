from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from pinax.images.models import ImageSet
from pinax.likes.models import Like

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


class TestLikes(TestCase):

    def setUp(self):
        super(TestLikes, self).setUp()
        self.user = self.make_user("cirrus")
        self.cloud_type = "cumulonimbus"
        self.spotting = CloudSpotting.objects.create(
            cloud_type=self.cloud_type,
            user=self.user,
            image_set=ImageSet.objects.create(created_by=self.user)
        )
        self.content_type = ContentType.objects.get(model="cloudspotting")

    def test_detail_like(self):
        """
        Ensure rendered detail contains expected "like" text.
        """
        with self.login(self.user):
            # Get detail for a not-liked collection.
            response = self.get("cloudspotting_detail", pk=self.spotting.pk)
            self.response_200()
            self.assertIn(b"Like", response.content)
            self.assertNotIn(b"Unlike", response.content)

            # Like the collection
            Like.objects.create(
                sender=self.user,
                receiver_content_type=self.content_type,
                receiver_object_id=self.spotting.pk
            )
            # Make sure the Like/Unlike value has toggled to "Unlike"
            response = self.get("cloudspotting_detail", pk=self.spotting.pk)
            self.response_200()
            self.assertIn(b"Unlike", response.content)
            self.assertNotIn(b"Like", response.content)

    def test_list_like(self):
        """
        Ensure rendered list contains expected "like" text.
        """
        with self.login(self.user):
            # List a not-liked collection.
            response = self.get("cloudspotting_list")
            self.response_200()
            self.assertNotIn(b"(liked)", response.content)

            # Like the collection
            Like.objects.create(
                sender=self.user,
                receiver_content_type=self.content_type,
                receiver_object_id=self.spotting.pk
            )
            # Make sure the Like/Unlike value has toggled to "Unlike"
            response = self.get("cloudspotting_list")
            self.response_200()
            self.assertIn(b"(liked)", response.content)
