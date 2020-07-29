from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView,  ValidateTokenAPIView, SetPasswordAPIView, GetUsersAPIView, ResendEmailAPIView


urlpatterns = [

    path('users/login/', LoginAPIView.as_view()),
    path('user/validate-token/<uuid:token>/',  ValidateTokenAPIView.as_view()),
    path('user/set-password/', SetPasswordAPIView.as_view()),
    path('users/register/', RegistrationAPIView.as_view()),
    # path('user/forgot-password/', ForgotPassword.as_view()),
    path('users/', GetUsersAPIView.as_view()),
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/resend-email/', ResendEmailAPIView.as_view())

]
