from django.shortcuts import render
from . import views


from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.home.serializers import OrganizationSerializer, ControlSerializer, UserprofileSerializer
from apps.home.models import Organization, Control, UserProfile

import logging

logger = logging.getLogger(__name__)

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Organization':'/org-overview/',
        'Organization Update':'/organization-update/',
        'Controls':'/controls-overview/',
        'Control':'/control-view/<str:pk>/',
        'Update':'/control-update/<str:pk>/',
        'User Update':'/userprofile-update/'
    }
    return Response(api_urls)

@api_view(['GET'])
def organization_view(request):
    org = Organization.objects.get(name=request.user.userprofile.organization.name)
    serializer = OrganizationSerializer(org, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def organization_update(request):
    org = Organization.objects.get(name=request.user.userprofile.organization.name)

    serializer = OrganizationSerializer(instance=org, data=request.data)

    if serializer.is_valid():
        serializer.save()
    print(serializer.errors)

    return Response(serializer.data)

@api_view(['POST'])
def userprofile_update(request):
    user = request.user.userprofile

    serializer = UserprofileSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
    print(serializer.errors)

    return Response(serializer.data)
    

@api_view(['GET'])
def controls_overview(request):
    org = Organization.objects.get(name=request.user.userprofile.organization.name)
    controls = org.control_set.all()
    serializer = ControlSerializer(controls, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def control_view(request, pk):
    org = Organization.objects.get(name=request.user.userprofile.organization.name)
    controls = org.control_set.all()
    control = controls.get(control_id=pk)
    serializer = ControlSerializer(control, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def control_update(request, pk):
    org = Organization.objects.get(name=request.user.userprofile.organization.name)
    controls = org.control_set.all()
    control = controls.get(control_id=pk)

    serializer = ControlSerializer(instance=control, data=request.data)

    if serializer.is_valid():
        print("I MADE IT")
        serializer.save()
    print(serializer.errors)

    return Response(serializer.data)