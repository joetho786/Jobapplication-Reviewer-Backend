from .models import Candidate
from rest_framework import viewsets, permissions
from .serializers import CandidateSerializer
from .permissions import IsOwnerOrReadOnly
# Candidate Viewset
class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    permission_classes = [
        # permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
        permissions.AllowAny,
    ]
    serializer_class = CandidateSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']
