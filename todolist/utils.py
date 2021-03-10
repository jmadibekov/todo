from django.core import exceptions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


# Create custom exception handler for rest_framework
# to handle custom ValidationError-s in models
def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is None and isinstance(exc, exceptions.ValidationError):
        return Response({"error": exc.message}, status=status.HTTP_400_BAD_REQUEST)

    return response
