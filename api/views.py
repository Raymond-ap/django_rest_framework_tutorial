from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer

from .models import Task


@api_view(['GET', 'POST'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list',
        'Detail view': '/task-detail/<slug:slug>/',
        'Create': '/task-create/<slug:slug>/',
        'Update': '/taks-update/<slug:slug>/',
        'Delete': '/task-delete/<slug:slug>/'
    }

    return Response(api_urls)


@api_view(['GET', 'POST'])
def TaskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TaskDetail(request, pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def TaskDelete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    serializer = TaskSerializer()
    return Response('Task deleted')
