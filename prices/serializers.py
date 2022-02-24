from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from prices.models import User, FileDetail


class UserSignUpSerializer(serializers.ModelSerializer):
    """
    Serializer for signup users endpoint.
    """
    password = serializers.CharField(write_only=True, required=True, help_text='Enter password',
                                     validators=[validate_password], style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, help_text='Renter password',
                                             validators=[validate_password], style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email',
            'password', 'confirm_password'
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],

        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class FileProcessSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = FileDetail
        fields = ('user', 'file', 'upload_date')
