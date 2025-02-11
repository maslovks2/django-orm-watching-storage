# Big Bald Brazzer Wathes You

Система **"Большой Лысый Брат Видит Тебя"** для организации пропускной системы на режимных объектах. 
Позволяет:
* вести учет активных пропусков
* просматривать историю входов-выходов по каждому пропуску
* позволяет видеть всех пользователей, которые зашли на охраняемый объект, но еще не вышли

Ниже можно найти инструкции для разворачивания окружения через PIP и [Poetry](https://python-poetry.org/docs/)

---
Для корректной работы потребуется Python версии 3.4, 3.5, 3.6 или 3.7
## Установка зависимостей через PIP из запуск из виртуального окружения

### 1. Создать виртуальное окружение
Для разворачивания приложения из корневой директории проекта необходимо создать виртуальное окружение

#### Создание виртуального окуржения 
```bash
    python -m venv .venv
```

### 2. Активировать виртуальное окружение

#### Для Mac/Linux
```bash
    source .venv/bin/activate
```


#### Для Windows
```bash
    venv\Scripts\activate.bat
```

### 3. Установить зависимостей через PIP
```bash
    pip install -r requirements.txt
```

### 4. Запуск приложения в активированном окружениии
```bash
    python manage.py runserver
```
---
## Установка через poetry
Для корректной работы потребуется poetry версии 1.1
### 1. Установка зависимостей
```bash
    poetry install
```
### 2. Запуск через виртуальное окружение *poetry*
```bash
    poetry run python manage.py runserver
```

## Переменные окружения

Для корректной работы нужно определить следующие переменные окружения 

[SECRET_KEY](https://docs.djangoproject.com/en/2.2/ref/settings/#secret-key)

[DB_URL](https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls)

[DEBUG](https://docs.djangoproject.com/en/2.2/ref/settings/#debug)

[ALLOWED_HOSTS](https://docs.djangoproject.com/en/2.2/ref/settings/#ALLOWED_HOSTS)
