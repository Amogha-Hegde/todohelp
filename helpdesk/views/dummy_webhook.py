from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def dummy_webhook(request, *args, **kwargs):
    echostr = request.query_params.get('echostr')
    return Response(data={echostr}, status=status.HTTP_200_OK)
