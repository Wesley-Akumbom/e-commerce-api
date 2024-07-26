from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, default='customer')

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'address', 'gender', 'contact', 'role', 'created_at',
                  'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', None)  # Remove the 'password' field from the serialized data
        return data
