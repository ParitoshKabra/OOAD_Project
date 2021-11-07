from rest_framework import routers
from shopBackend.models import Log
from .views import ItemApiViewSet, ItemCommentViewSet, LogApiViewSet, CommentApiViewSet, NotificationApiViewSet, UserApiViewSet
router = routers.DefaultRouter()

router.register("items", ItemApiViewSet)
router.register("comments", CommentApiViewSet)
router.register("notifications", NotificationApiViewSet)
router.register("logs", LogApiViewSet)
router.register("item_cnot", ItemCommentViewSet)

router.register("users", UserApiViewSet)
