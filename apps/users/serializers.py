from rest_framework import serializers
from apps.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'name']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered")
        return value
    
    def create(self,validated_data):
        password=validated_data.pop('password')
        user=User(**validated_data) #instance of User || ** represents spreading dict data as params
        user.set_password(password) #hashing password
        user.save()
        return user
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'id',
            'email',
            'name',
            'role',
            'phone',
            'gender',
            'occupation',
            'languages',
        ]

class RoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['role']


    