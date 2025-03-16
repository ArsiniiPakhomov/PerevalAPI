from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Coords, Pereval
# Image
from django.core.files.uploadedfile import SimpleUploadedFile

class ModelTests(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create(
            email='test@example.com',
            last_name='Иванов',
            first_name='Иван',
            middle_name='Иванович',
            phone='1234567890'
        )

        # Создаем тестовые координаты
        self.coords = Coords.objects.create(
            latitude=55.7558,
            longitude=37.6176,
            height=150
        )

        # Создаем тестовый перевал
        self.pereval = Pereval.objects.create(
            status=Pereval.NEW,
            user=self.user,
            coords=self.coords,
            beauty_title='Тестовый перевал',
            title='Перевал Тестовый',
            other_titles='Другие названия',
            connect='Сопроводительный текст',
            level_spring='1A',
            level_summer='2A',
            level_autumn='3A',
            level_winter='4A'
        )

        # Создаем тестовое изображение
        # self.image = Image.objects.create(
        #     pereval=self.pereval,
        #     data=SimpleUploadedFile('test_image.jpg', b'file_content', content_type='image/jpeg'),
        #     title='Тестовое изображение'
        # )

        # Инициализируем APIClient
        self.client = APIClient()

    def test_user_creation(self):
        """Тест создания пользователя."""
        user = User.objects.get(email='test@example.com')
        self.assertEqual(user.last_name, 'Иванов')
        self.assertEqual(user.first_name, 'Иван')
        self.assertEqual(user.middle_name, 'Иванович')
        self.assertEqual(user.phone, '1234567890')

    def test_coords_creation(self):
        """Тест создания координат."""
        coords = Coords.objects.get(id=self.coords.id)
        self.assertEqual(coords.latitude, 55.7558)
        self.assertEqual(coords.longitude, 37.6176)
        self.assertEqual(coords.height, 150)

    def test_pereval_creation(self):
        """Тест создания перевала."""
        pereval = Pereval.objects.get(id=self.pereval.id)
        self.assertEqual(pereval.beauty_title, 'Тестовый перевал')
        self.assertEqual(pereval.title, 'Перевал Тестовый')
        self.assertEqual(pereval.other_titles, 'Другие названия')
        self.assertEqual(pereval.connect, 'Сопроводительный текст')
        self.assertEqual(pereval.level_spring, '1A')
        self.assertEqual(pereval.level_summer, '2A')
        self.assertEqual(pereval.level_autumn, '3A')
        self.assertEqual(pereval.level_winter, '4A')

    # def test_image_creation(self):
    #     """Тест создания изображения."""
    #     image = Image.objects.get(id=self.image.id)
    #     self.assertEqual(image.title, 'Тестовое изображение')
    #     self.assertEqual(image.pereval, self.pereval)

    def test_pereval_status_update(self):
        """Тест обновления статуса перевала."""
        pereval = Pereval.objects.get(id=self.pereval.id)
        pereval.status = Pereval.ACCEPTED
        pereval.save()
        updated_pereval = Pereval.objects.get(id=self.pereval.id)
        self.assertEqual(updated_pereval.status, Pereval.ACCEPTED)

    def test_pereval_delete(self):
        """Тест удаления перевала."""
        pereval_id = self.pereval.id
        self.pereval.delete()
        with self.assertRaises(Pereval.DoesNotExist):
            Pereval.objects.get(id=pereval_id)

    # def test_image_delete(self):
    #     """Тест удаления изображения."""
    #     image_id = self.image.id
    #     self.image.delete()
    #     with self.assertRaises(Image.DoesNotExist):
    #         Image.objects.get(id=image_id)

    def test_pereval_list_api(self):
        """Тест API для получения списка перевалов."""
        url = reverse('pereval-list-create')  # Убедитесь, что у вас есть URL для списка перевалов
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Проверяем, что возвращается один перевал

    def test_pereval_detail_api(self):
        """Тест API для получения деталей перевала."""
        url = reverse('pereval-detail', args=[self.pereval.id])  # Убедитесь, что у вас есть URL для деталей перевала
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Перевал Тестовый')

    def test_pereval_create_api(self):
        """Тест API для создания перевала."""
        url = reverse('pereval-list-create')  # Убедитесь, что у вас есть URL для создания перевала
        data = {
            'status': Pereval.NEW,
            'user': self.user.id,
            'coords': self.coords.id,
            'beauty_title': 'Новый перевал',
            'title': 'Перевал Новый',
            'other_titles': 'Другие названия',
            'connect': 'Сопроводительный текст',
            'level_spring': '1A',
            'level_summer': '2A',
            'level_autumn': '3A',
            'level_winter': '4A',
             'image': [
            {
                'data': SimpleUploadedFile('test_image.jpg', b'file_content', content_type='image/'),
                'title': 'Тестовое изображение'
            }
        ]
        }
        response = self.client.post(url, data, format='multipart')  # Используйте 'multipart' для загрузки файлов
        response = self.client.post(url, data, format='json')
        print(response.data) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pereval.objects.count(), 2)  # Проверяем, что перевал создан

    def test_pereval_update_api(self):
        """Тест API для обновления перевала."""
        url = reverse('pereval-detail', args=[self.pereval.id])  # Убедитесь, что у вас есть URL для обновления перевала
        data = {
            'title': 'Обновленный перевал'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_pereval = Pereval.objects.get(id=self.pereval.id)
        self.assertEqual(updated_pereval.title, 'Обновленный перевал')

    def test_pereval_delete_api(self):
        """Тест API для удаления перевала."""
        url = reverse('pereval-detail', args=[self.pereval.id])  # Убедитесь, что у вас есть URL для удаления перевала
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pereval.objects.count(), 0)  # Проверяем, что перевал удален