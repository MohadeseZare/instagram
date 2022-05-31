from rest_framework import viewsets
from .models import ScheduledPost


class ScheduledPostViewSet(viewsets.ModelViewSet):
    queryset = ScheduledPost.objects.all()
