from core.service import VersionDefaultRouter
from work import views

router = VersionDefaultRouter()
router.register('', views.WorkViewSet, basename='work')
