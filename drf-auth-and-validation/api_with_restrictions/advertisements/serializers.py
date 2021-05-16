from django.contrib.auth.models import User
from rest_framework import serializers
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        # Необходимо валидировать, что у пользователя не больше 10 открытых объявлений.
        """Метод для валидации. Вызывается при создании и обновлении."""
        creator = self.context["request"].user
        order_quantity = len(list(Advertisement.objects.filter(creator=creator, status="OPEN")))
        if self.context["request"].method == "POST" and order_quantity >= 10:
            raise serializers.ValidationError(f'У пользователя превышено количество открытых заказов')
        else:
            return data
