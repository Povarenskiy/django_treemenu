# Django Tree Menu

django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
````
{% draw_menu 'main_menu' %}
````
Реализован на Python 3.10. Используются только Django и стандартные библиотеки Python.


## 1 Установка

Клонировать репозиторий с Github.com, перейти в проект 
````
git clone https://github.com/Povarenskiy/django_treemenu.git
cd django_treemenu
````

### 1.1 Установка через poetry
````
poetry install
poetry shell
````

### 1.2 Установка через pip
````
python -m venv venv                 # создать виртуальное оркужение

venv\Scripts\activate               # активация venv для Windows
source venv/bin/activate            # активация venv для Linux

pip install -r requirements.txt     # установка зависимостей
````

## 2 Запуск

````
python manage.py migrate            # миграции в базу данных
python manage.py createsuperuser    # создать пользователя 
...
python manage.py runserver          # запустить сервер
````

## 3 URL
Сайт: ````http://localhost:8000/````
Панель администратора: ````http://localhost:8000/admin/````
