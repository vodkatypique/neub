from rest_framework import routers
from hmc import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('clubs', views.ClubsViewSet)
router.register('players', views.PlayersViewSet)
router.register('draft', views.ClassedraftViewSet)
router.register('formations', views.FormationViewSet)
router.register('roles', views.RoleViewSet)
router.register('tactic', views.TacticViewSet)
