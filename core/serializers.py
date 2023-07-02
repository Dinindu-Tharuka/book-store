from djoser.serializers import UserCreateSerializer as UserCreate


class UserCreateSerializer(UserCreate):
    class Meta(UserCreate.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email']
