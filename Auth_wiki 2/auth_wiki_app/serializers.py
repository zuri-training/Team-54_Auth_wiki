
from rest_framework import serializers
from .models import User
import uuid


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        allow_blank = True

        fields = [ "email", "uuid", "first_name", "last_name", "password"]
        read_only_fields = ['uuid']
    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                       first_name=validated_data['first_name'],
                                       last_name=validated_data['last_name'],
                                        uuid = str(uuid.uuid4()).replace('-', '')
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user