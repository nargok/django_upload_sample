from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer
import os


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        file_obj = request.FILES['file']

        filename = os.path.join(settings.MEDIA_ROOT, file_obj.name)
        with open(filename, 'wb+') as temp_file:
            for chunk in file_obj.chunks():
                temp_file.write(chunk)

        if file_serializer.is_valid():
            return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
