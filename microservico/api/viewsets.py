from microservico.api.serializers import (ActionsSerializer, MessageSerializer,
                                          UserSerializer)
from microservico.models import Actions, Message, User
from rest_framework import viewsets


class ActionsViewSet(viewsets.ModelViewSet):
    queryset = Actions.objects.raw("""SELECT * FROM
     microservico_actions""") 
    serializer_class = ActionsSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.raw("""SELECT * FROM
     microservico_message""") 
    serializer_class = MessageSerializer

class UsersViewSet(viewsets.ModelViewSet): 
    queryset = User.objects.raw("""SELECT * FROM
     microservico_user""") 
    serializer_class = UserSerializer 
    

 