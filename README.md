## Приложение Notes 
- асинхронное веб-приложение на основе FastAPI, которое предоставляет сервис по управлению личными заметками.
- Телеграмм-бот который связывается с приложением путем ввода логина и пароля единажды, после этого устанавливается связь между аккаунтом ТГ и прижении 
Тг-бот непосредственно независимое приложение способное работать автономно от основного 
## Функционал
- В приложение можно:
    - Регистрироваться
    - Авторизовываться (авторизация выполнена через JWT)
    - Создавать, удалять, редактировать запись
    - Просматривать все свои записи
    - искать все записи по Тегу

- В ТГ-боте можно:
    - Регисрироваться
    - Авторизовываться
    - Создавать записи
    - Просматривать все свои записи
    - Искать все записи по Тегу
Все общение спользователем (кроме ввода данных) осуществляется через inline клавиатуру.

## Используемые технологии 
Язык: Python
Frameworks: FastApi, Aiogram
База данных: Postgesql

Docler, docker-compose

## Запуск приложения
- скачиваем оба репозитория 
    ТГ-бот: https://github.com/Fedetsov-Ruslan/notes_tg
    FastApi: https://github.com/Fedetsov-Ruslan/notes_fastAPI

    в каждом из приложений создаем файо .env, переносим туда переменные из .env.example
    в ТГ-боте прописываем собственный TG_TOKEN= 
    
затем
- в Тг-бот испльзуем команду:  docker build -t notes_tg:latest . 
- затем в FastAPI: docker-compose up --build 


