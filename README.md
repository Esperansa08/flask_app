# Anime app
![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=flat&logo=jinja&logoColor=black)
![REST](https://img.shields.io/badge/-REST-464646?style=flat&logo=REST&logoColor=black)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)

 Проект "Антиматека" хранит и предоставляет информацию об аниме,
создан с применением фреймворка Flask и SQLAlchemy.

Доступ осуществляется через веб-сайт или посредством API.

### Содержание:
- [Anime app](#anime-app)
    - [Содержание:](#содержание)
  - [Ключевые возможности сервиса](#ключевые-возможности-сервиса)
  - [Как установить программу](#как-установить-программу)
  - [Автор](#автор)

## Ключевые возможности сервиса
- Пользователь на главной странице видит случайное аниме из базы приложения (название и описание),
а также случайное аниме Кинопоиска(название и описание).
- Доступен список всех аниме
- добавление нового аниме, изменение и удаление из базы


Доступны web и api интерфейсы.

## Как установить программу

Системные требования:

- Python==3.7.9
- sqlalchemy==1.4.29
- flask==2.0.2

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Esperansa08/flask_app.git

```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Должен быть запущен докер

Запустить программу:

```
docker-compose up -d
```
Создаем базу и заполняем тестовыми данными:

```
python connector.py

```
Приложение будет доступно по адресу: http://localhost:5000/

```

## Автор

 * Савельева Анастасия ([Почта](Visteria09@yandex.ru), [Github](https://github.com/Esperansa08))
