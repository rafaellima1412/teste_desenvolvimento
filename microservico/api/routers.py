from microservico.api.viewsets import (ActionsViewSet, MessageViewSet,
                                       UsersViewSet)
from rest_framework import routers

router = routers.DefaultRouter()

router.register('actions', ActionsViewSet)
router.register('user', UsersViewSet)
router.register('message', MessageViewSet)
