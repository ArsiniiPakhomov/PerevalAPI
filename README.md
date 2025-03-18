#  Pereval API

**REST API для учёта и модерации горных перевалов**  
Серверная часть системы, позволяющая туристам добавлять данные о перевалах, а модераторам — проверять их.

---

## Задача проекта

Разработать API для мобильного приложения, которое:
1. Позволяет пользователям добавлять информацию о перевалах (координаты, фото, уровень сложности).
2. Обеспечивает модерацию данных через изменение статуса записей.
3. Запрещает редактирование данных после прохождения модерации.

---

## Возможности API

### Основные методы:
 
 - `POST` `/submitData/`  Добавление нового перевала 
 - `GET`  `/submitData/<id>/`  Получение данных по ID 
-  `PATCH`  `/submitData/<id>/update/`  Редактирование (только статус `new`) 
-  `GET`  `/submitData/list/?user__email=<email>`  Фильтрация по email пользователя 

### Ключевые особенности: 
✅ Валидация координат и уровней сложности  
✅ Автоматический статус `new` для новых записей  
✅ Защита от изменения персональных данных  
✅ Поддержка PostgreSQL

---

## Технологии

![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-red?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)


---

## Быстрый старт

### Установка
- прокт написан на python v 3.12.2
- создание виртуального окружения python -m venv .venv
- перейти в виртуальное окружение .venv\scripts\activate
- скачать git
- git clone https://github.com/ArsiniiPakhomov/MMO_RPG-Board.git
- cd project_per
- затем загрузить библиотеки указанные в файле requirements.txt

---
## Начало работы с БД 
- установить PostgresSQL(лучше сразу же СУБД PgAdmin4)
- в файле settings.py в DATABASES эти поля заменить на свои значения 
- 'USER': os.getenv('FSTR_DB_LOGIN'),      # Имя пользователя PostgreSQL
- 'PASSWORD': os.getenv('FSTR_DB_PASS'),   # Пароль пользователя
- 'HOST': os.getenv('FSTR_DB_HOST'),       # Хост (если база на локальной машине то: localhost)
- 'PORT': os.getenv('FSTR_DB_PORT'),       # Порт (по умолчанию 5432)
