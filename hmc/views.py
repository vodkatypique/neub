from django.shortcuts import render
from django.views.generic import *
from rest_framework.response import Response

from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from .serializers import *
from rest_framework.generics import *
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PlayersViewSet(viewsets.ModelViewSet):
    queryset = HmcPlayers.objects.all()
    serializer_class = HmcPlayersSerializer


class ClubsViewSet(viewsets.ModelViewSet):
    queryset = HmcClubs.objects.all()
    serializer_class = HmcClubSerializer

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        print(request.data)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class ClassedraftViewSet(viewsets.ModelViewSet):
    queryset = HmcClassedraft.objects.all()
    serializer_class = HmcClassedraftSerializer


class FormationViewSet(viewsets.ModelViewSet):
    queryset = HmcFormations.objects.all()
    serializer_class = HmcFormationsSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = HmcRoles.objects.all()
    serializer_class = HmcRolesSerializer


class TacticViewSet(viewsets.ModelViewSet):
    queryset = HmcTactics.objects.all()
    serializer_class = HmcTacticsSerializer

