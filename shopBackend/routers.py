from rest_framework import routers
from shopBackend.models import Log
from .views import ItemApiViewSet, LogApiViewSet, CommentApiViewSet, NotificationApiViewSet
router = routers.DefaultRouter()

router.register("items", ItemApiViewSet)
router.register("comments", CommentApiViewSet)
router.register("notifications", NotificationApiViewSet)
router.register("logs", LogApiViewSet)
router.register("users", UserApiViewSet)