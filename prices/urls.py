from django.urls import path

from prices.views import FileProcessAPIView, UserSignUpAPIView

urlpatterns = [
    path('', FileProcessAPIView.as_view(), name='upload-file'),
    path('signup/', UserSignUpAPIView.as_view(), name='signup')
]
