from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        fields = ['user', 'bio', 'location']

class RegistrationSerializers(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password':{
                'write_only' : True
            }
        }

    def save(self):
        pw = self.validated_data['password']
        repeated_password = self.validated_data['repeated_password']

        if pw != repeated_password:
            raise serializers.ValidationError({'error':'passwords dont match'})

        account = User(email = self.validated_data['email'], username = self.validated_data['username'])
        account.set_password(pw)
        account.save()
        return account

    def validate_email(self,value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError({'error':'Die Email-Adresse existiert bereits'})
        return value
