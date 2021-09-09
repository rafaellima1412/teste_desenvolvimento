from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from webapi.exceptions import PythonDjangoException

from microservico.api.serializers import UserSerializer
from microservico.models import Actions, Message, User


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


@api_view(["POST"])
def signup(request, **kwargs):
    try:
        serializer = UserSerializer(data=request.data)
        response = Response()
        if serializer.is_valid():
            messages = request.data.pop("message")
            data_user = request.data
            user = User.objects.create_user(**data_user)
            for message in messages:
                p = Message(
                    destination_user_id=message["destination_user_id"],
                    message=message["message"],
                    user_id=user,
                )
                p.save()

            return Response(data=response.data, status=status.HTTP_201_CREATED)
        else:
            raise PythonDjangoException(
                message=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE
            )
    except PythonDjangoException as e:
        return Response(e.detail, status=e.status_code)
    except APIException as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
# @permission_classes([AllowAny])
def signin(request):
    try:
        name = request.data.get("name")
        password = request.data.get("password")
        response = Response()
        if (name is None) or (password is None):
            raise PythonDjangoException(
                message="name and password required",
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(name=name).first()
        if user is None:
            raise PythonDjangoException(
                message="name not found", status=status.HTTP_400_BAD_REQUEST
            )
        if not user.check_password(password):
            raise PythonDjangoException(
                message="Wrong password", status=status.HTTP_400_BAD_REQUEST
            )

        return Response(data=response.data, status=status.HTTP_200_OK)
    except PythonDjangoException as e:
        return Response(e.detail, status=e.status_code)
    except APIException as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
