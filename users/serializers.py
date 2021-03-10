from django.contrib.auth import authenticate
from django.db import IntegrityError, DatabaseError

from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'is_staff', 'email', 'password', 'created_at', 'updated_at')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def save(self, **kwargs):
        try:
            instance = super().save(**kwargs)
        except (IntegrityError, DatabaseError):
            raise serializers.ValidationError({'message': 'Email already used, please use a different one'})
        instance.set_password(self.validated_data['password'])
        instance.save()
        return instance

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'auth_token',
        )
        read_only_fields = ('auth_token',)


class SignInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.pop('email')
        password = attrs.pop('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'auth_token',
            'password'
        )
        read_only_fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'auth_token',
        )
