from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from django.contrib import admin
from pinax.images import urls
from . import views


urlpatterns = [
    url(r"^$", views.Home.as_view(), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^ajax/images/", include("pinax.images.urls", namespace="pinax_images")),
    url(r"^likes/", include("pinax.likes.urls", namespace="pinax_likes")),
    url(r"^announcements/", include("pinax.announcements.urls", namespace="pinax_announcements")),
    url(r"^messages/", include("pinax.messages.urls", namespace="pinax_messages")),

    url(r"^cloudspotting/$",
        views.CloudSpottingListView.as_view(),
        name="cloudspotting_list"),
    url(r"^cloudspotting/create/$",
        views.CloudSpottingCreateView.as_view(),
        name="cloudspotting_create"),
    url(r"^cloudspotting/(?P<pk>\d+)/$",
        views.CloudSpottingDetailView.as_view(),
        name="cloudspotting_detail"),
    url(r"^cloudspotting/(?P<pk>\d+)/update/$",
        views.CloudSpottingUpdateView.as_view(),
        name="cloudspotting_update"),
    url(r"^cloudspotting/(?P<pk>\d+)/delete/$",
        views.CloudSpottingDeleteView.as_view(),
        name="cloudspotting_delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
