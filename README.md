# Django Tree Menu

django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
````
{% draw_menu 'main_menu' %}
````
Реализован на Python 3.10. Используются только Django и стандартные библиотеки Python.


## 1 Установка и запуск

Клонировать репозиторий с Github.com, в директории проекта настроить виртуальное окружение через poetry 
````
git clone https://github.com/Povarenskiy/django_treemenu.git
cd django_treemenu
poetry install
poetry shell
````

Запустить проект, предварительно создав пользователя для входа в панель администратора 
````
python manage.py migrate            # миграции в базу данных
python manage.py createsuperuser    # создать администатора
...
python manage.py runserver          # запустить сервер
````

## 3 URL

Сайт: [http://localhost:8000/](http://localhost:8000/) 

Панель администратора: [http://localhost:8000/](http://localhost:8000/admin/) 
