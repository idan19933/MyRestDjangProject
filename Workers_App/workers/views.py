from django.shortcuts import render
from .models import Workers
from rest_framework import viewsets,permissions
from .models import Workers
from .serializers import WorkersSerializers


def home_view(request):
    workers = Workers.objects.all()
    return render(request,'workers_list/home.html/',{'workers':workers})


def detail_view(request,slug):
    worker = Workers.objects.get(slug=slug)
    return render(request, 'workers_list/detail.html', {'worker': worker})

def index_view(request):
    return render(request,'workers_list/index.html/')


class WorkersView(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)







