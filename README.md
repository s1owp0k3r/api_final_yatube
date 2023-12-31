# YaTube API
## Описание
YaTube API предоставляет интерфейс для работы с блогом YaTube: возможность добавления, просмотра, редактирования и удаления постов и комментариев, а также возможность подписки на других авторов.
## Установка
- Клонируйте проект из гитхаба:\
`git clone git@github.com:s1owp0k3r/api_final_yatube.git`
- Создайте и активируйте виртуальное окружение:\
`python -m venv venv`\
`source venv/Scripts/activate`
- Установите зависимости из файла requirements.txt:\
`pip install -r requirements.txt`
- Перейдите в каталог с файлом manage.py, примените миграции:\
`cd yatube_api/`\
`python manage.py migrate`
- Запустите сервер:\
`python manage.py runserver`
## Примеры запросов
- GET /api/v1/posts/ - Получить список всех публикаций.
- POST /api/v1/posts/ - Добавление новой публикации в коллекцию публикаций.
- GET /api/v1/posts/{post_id}/comments/ - Получение всех комментариев к публикации.
- POST /api/v1/posts/{post_id}/comments/ - Добавление нового комментария к публикации.
- GET /api/v1/posts/{post_id}/comments/{id}/ - Получение комментария к публикации по id.
## Авторы
- Борис Градов
## Используемые технологии
Проект создан с использованием Django Rest Framework, аутентификация пользователей осуществляется через jwt-токены при помощи библиотеки djoser.
