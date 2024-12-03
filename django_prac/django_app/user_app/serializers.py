from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email = self.validated_data['email']

        if password != password2:
            raise serializers.ValidationError("Password and password2 should be same")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Same Email already exists")

        user = User(email=email, username=self.validated_data['username'])
        user.set_password(password)
        user.save()
        return user
