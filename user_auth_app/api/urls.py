from django.urls import path
from .views import UserProfileList,UserProfileDetailAccess, RegistrationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name= 'userprofile-list'),
    path('profiles/<int:pk>/', UserProfileDetailAccess.as_view(), name = 'userprofile-detail'),
    path('registration/', RegistrationView.as_view(), name = 'registration'),
    path('login/', obtain_auth_token, name='login')
]
