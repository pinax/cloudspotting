from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from pinax.images.models import ImageSet

from .models import CloudSpotting


class Home(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("cloudspotting_list"))
        return super(Home, self).get(request, *args, **kwargs)


class CloudSpottingCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new CloudSpotting collection.
    """
    model = CloudSpotting
    fields = ["cloud_type"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image_set = ImageSet.objects.create(created_by=self.request.user)
        return super(CloudSpottingCreateView, self).form_valid(form)


class CloudSpottingDetailView(LoginRequiredMixin, DetailView):
    """
    Display a specific CloudSpotting collection.
    """
    model = CloudSpotting


class CloudSpottingListView(LoginRequiredMixin, ListView):
    """
    Display a list of CloudSpotting collections.
    """
    model = CloudSpotting


class UserCloudSpottingMixin(LoginRequiredMixin):
    """
    Constrains user to just their own Cloudspottings.
    """
    model = CloudSpotting

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class CloudSpottingUpdateView(UserCloudSpottingMixin, UpdateView):
    """
    Update details about a CloudSpotting collection.
    """
    fields = ["cloud_type"]


class CloudSpottingDeleteView(UserCloudSpottingMixin, DeleteView):
    """
    Delete a CloudSpotting collection.
    """
    success_url = reverse_lazy("cloudspotting_list")
