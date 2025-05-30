# backend_community_homework
# Cоциальная сеть Yatube

## Описание

Позволяет авторам создавать записи на различные темы,дает возможность комментировать их и подписываться/отписываться от авторов.Включает в себя администрирование, управление пользователями, работу с записями(создание, редактирование, удаление), объединение записей по сообществам, паджинацию, модель отправки электронных сообщений пользователям, основные шаблоны для страниц сайта.Для хранение данных используется SQLite.

#### Технологии

- Python 3.7
- Django 2.2.16

#### Запуск проекта в dev-режиме

- Склонируйте репозиторий:  
``` git clone <название репозитория> ```
- Установите и активируйте виртуальное окружение:  
``` python -m venv venv ```  
``` source venv/Scripts/activate ```
- Установите зависимости из файла requirements.txt:
``` pip install -r requirements.txt ```
- Перейдите в папку yatube/yatube.
- Примените миграции:  
``` python manage.py makemigrations ```  
``` python manage.py migrate ```
- Выполните команду:
``` python manage.py runserver ```
[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)
