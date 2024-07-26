from rest_framework import serializers

from .models import Store

from api.apps.user.serializers import UserSerializer


class StoreSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Store
        fields = '__all__'
