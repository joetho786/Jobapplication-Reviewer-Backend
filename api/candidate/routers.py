from rest_framework import routers
from api.candidate.viewsets import CandidateViewSet

router = routers.SimpleRouter(trailing_slash=False)

# create/edit/delete candidate router
router.register(r"candidate", CandidateViewSet, basename="candidate")

urlpatterns = [
    *router.urls,
]