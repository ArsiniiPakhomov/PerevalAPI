from rest_framework import serializers
from .models import User, Coords, Image, Pereval

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'last_name', 'first_name', 'middle_name', 'phone']

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = [ 'latitude', 'longitude', 'height']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['data', 'title']

class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    images = ImageSerializer(many=True, source='attached_images')  # Используем related_name

    class Meta:
        model = Pereval
        fields = [
            'id', 'status', 'user', 'coords', 'beauty_title', 'title', 
            'other_titles', 'connect', 'datetime', 'level_spring', 
            'level_summer', 'level_autumn', 'level_winter', 'images'
        ]

    def create(self, validated_data):
        # Извлекаем данные для вложенных моделей
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        images_data = validated_data.pop('attached_images')

        # Создаём объекты User и Coords
        user = User.objects.create(**user_data)
        coords = Coords.objects.create(**coords_data)

        # Создаём объект Pereval
        pereval = Pereval.objects.create(user=user, coords=coords, **validated_data)

        # Создаём объекты Image
        for image_data in images_data:
            Image.objects.create(pereval=pereval, **image_data)

        return pereval

    def update(self, instance, validated_data):
        # Обновляем данные Pereval
        instance.status = validated_data.get('status', instance.status)
        instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
        instance.title = validated_data.get('title', instance.title)
        instance.other_titles = validated_data.get('other_titles', instance.other_titles)
        instance.connect = validated_data.get('connect', instance.connect)
        instance.level_spring = validated_data.get('level_spring', instance.level_spring)
        instance.level_summer = validated_data.get('level_summer', instance.level_summer)
        instance.level_autumn = validated_data.get('level_autumn', instance.level_autumn)
        instance.level_winter = validated_data.get('level_winter', instance.level_winter)
        instance.save()

        # Обновляем данные Coords
        coords_data = validated_data.get('coords', {})
        coords = instance.coords
        coords.latitude = coords_data.get('latitude', coords.latitude)
        coords.longitude = coords_data.get('longitude', coords.longitude)
        coords.height = coords_data.get('height', coords.height)
        coords.save()

        # Обновляем данные User
        user_data = validated_data.get('user', {})
        user = instance.user
        user.email = user_data.get('email', user.email)
        user.last_name = user_data.get('last_name', user.last_name)
        user.first_name = user_data.get('first_name', user.first_name)
        user.middle_name = user_data.get('middle_name', user.middle_name)
        user.phone = user_data.get('phone', user.phone)
        user.save()

        # Обновляем изображения (если нужно)
        images_data = validated_data.get('attached_images', [])
        instance.attached_images.all().delete()  # Удаляем старые изображения
        for image_data in images_data:
            Image.objects.create(pereval=instance, **image_data)

        return instance