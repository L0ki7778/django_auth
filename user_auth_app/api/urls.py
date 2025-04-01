from django.urls import path
from .views import UserProfileList,UserProfileDetailAccess

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name= 'userprofile-list'),
    path('profiles/<int:pk>/', UserProfileDetailAccess.as_view(), name = 'userprofile-detail')
]
