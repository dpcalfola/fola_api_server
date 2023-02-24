from django.shortcuts import render  # noqa
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Api1View(APIView):
    """
    API endpoint that returns a message.
    """
    @staticmethod
    def get(request, number=None):
        """
        Return a message.
        :param request:
        :param number: None or integer for url path
        :return: data and status
        """
        if number is None:
            data = {'message': "Hello, REST API!"}
        else:
            data = {
                'message': f'Get a number: {number}',
                'number': number
            }
        return Response(data, status=status.HTTP_200_OK)
