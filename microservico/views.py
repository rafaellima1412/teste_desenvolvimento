from rest_framework.decorators import api_view
from rest_framework.response import Response
from webapi.exceptions import PythonDjangoException

from microservico.models import Actions, Message


# Sugestão de melhoria para usuarios logados aparecer suas proprias mesnagens
@api_view(["GET"])
def me(request, **kwargs):
    try:
        user = request.user
        response = {
            # "name": data_user.name,
            "message": Message.objects.values("message").filter(user_id=user.id),
        }
        return Response(data=response)
    except PythonDjangoException as e:
        return Response(e.detail, status=e.status_code)
