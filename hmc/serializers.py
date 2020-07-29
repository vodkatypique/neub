from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class HmcPlayersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HmcPlayers
        fields = '__all__'


class HmcClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = HmcClubs
        fields = ['url', 'id', 'pseudo', 'club', 'conference', 'logo', 'massebudget', 'massebudgetactuelle', 'formation', 'consign', 'compo', 'edited_at', 'screenclub', 'screeneffectif', 'screencalendrier', 'screencompet']


class HmcClassedraftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HmcClassedraft
        fields = ['url', 'name']


class HmcFormationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HmcFormations
        fields = ['url', 'formation', 'postes', 'idu']


class HmcRolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HmcRoles
        fields = ['url', 'poste', 'roles']


class HmcTacticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HmcTactics
        fields = ['url', 'idu', 'tactique', 'cons1', 'cons2', 'cons3']
