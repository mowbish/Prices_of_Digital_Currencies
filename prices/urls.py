from django.urls import path

from prices.views import FileUploadView, UserSignUpAPIView

urlpatterns = [
    path('', FileUploadView.as_view(), name='upload-file'),
    path('signup/', UserSignUpAPIView.as_view(), name='signup')
]
