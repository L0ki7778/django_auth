from rest_framework import generics
from rest_framework.views import APIView
from .serializers import UserProfileSerializer, RegistrationSerializers
from user_auth_app.models import UserProfile
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetailAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CustomLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = Token.objects.get(user = user)
            data = {
                'token':token.key,
                'username':user.username,
                'email': user.email
            }
        else:
            data= serializer.errors
        return Response(data)



class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializers(data = request.data)

        if serializer.is_valid():
            saved_account = serializer.save()
            token = Token.objects.create(user = saved_account)
            data = {
                'token': token.key,
                'username':saved_account.username,
                'email':saved_account.email
            }
        else:
            data = serializer.errors
        return Response(data)
