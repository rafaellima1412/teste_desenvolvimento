from rest_framework.decorators import api_view
from rest_framework.response import Response
from webapi.exceptions import PythonDjangoException

from microservico.models import Actions


# Sugestão de melhoria para usuarios logados aparecer suas proprias mesnagens
@api_view(["GET"])
def mine(request, **kwargs):
    try:
        data_user = request.user
        response = {
            "message": data_user.message,
            "likes": Actions.objects.values("like", "unlike").filter(
                user_id=data_user.id
            ),
        }
        return Response(data=response)
    except PythonDjangoException as e:
        return Response(e.detail, status=e.status_code)
