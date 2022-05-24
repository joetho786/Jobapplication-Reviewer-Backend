from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("api/users/", include(("api.routers", "api"), namespace="api")),
    path("api/", include(("api.candidate.routers","api.candidate"), namespace="candidate-api")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
