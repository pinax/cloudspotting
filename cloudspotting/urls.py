from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("ajax/images/", include("pinax.images.urls", namespace="pinax_images")),
    path("likes/", include("pinax.likes.urls", namespace="pinax_likes")),
    path("announcements/", include("pinax.announcements.urls", namespace="pinax_announcements")),
    path("messages/", include("pinax.messages.urls", namespace="pinax_messages")),

    path("cloudspotting/", include([
        path("", views.CloudSpottingListView.as_view(), name="cloudspotting_list"),
        path("create/", views.CloudSpottingCreateView.as_view(), name="cloudspotting_create"),
        path("<int:pk>/", views.CloudSpottingDetailView.as_view(), name="cloudspotting_detail"),
        path("<int:pk>/update/", views.CloudSpottingUpdateView.as_view(), name="cloudspotting_update"),
        path("<int:pk>/delete/", views.CloudSpottingDeleteView.as_view(), name="cloudspotting_delete"),
    ]))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
