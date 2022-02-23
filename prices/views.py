from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from prices.models import User, FileDetail
from prices.serializers import UserSignUpSerializer, FileDetailSerializer


class UserSignUpAPIView(CreateAPIView):
    """
        This class for register users.
        Users can log in and add comment,
        Report or like articles.
    """
    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()


class FileUploadView(ListCreateAPIView):
    # parser_classes = (FileUploadParser,)
    serializer_class = FileDetailSerializer
    permission_classes = (IsAuthenticated,)
    queryset = FileDetail.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def put(self, request, filename, format=None):
    # def post(self, request, *args, **kwargs):
    #     file_obj = request.FILES['file']
    #     # do some stuff with uploaded file
    #     return Response(status=204)
