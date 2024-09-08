from app.apps.dropbox.viewsets import FileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'files', FileViewSet, basename='files')

urlpatterns = router.urls