from rest_framework_json_api import serializers
from rest.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, allow_blank=False, allow_null=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',
                  'create_at', 'update_at')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_email(self, email):
        if email:
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    'Email already used.')

            return email
