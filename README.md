﻿        API ДЛЯ УПРАВЛЕНИЯ БИБЛИОТЕКОЙ

ОПИСАНИЕ:
Данная API упрощает работу библиотек
Сотрудники заносятся через ADMIN панель в отдельную группу Librarian
У сотрудников библиотеки более расширенные права доступа,
например они могут работать с обычными пользователями
Так же фильтрация книг и авторов упрощает поиск книг в наличии,
книг и авторов книг по определенным полям и др. 


====================================================

ТЕХНОЛОГИИ:

-Django 

-Django Rest Framework (DRF)

-JWT

-OpenAPIDocs

-PostgreSQL

-Docker

-Docker-compose
 

====================================================


Запуск через Docker

Инструкция:

1. Убедитесь, что Docker установлен на ваш компьютер, или установите из дистрибутива, полученного на сайте https://www.docker.com/. 

2. Для запуска процесса создания контейнеров в терминале перейдите в корневую папку проекта и выполните команду:
$ docker-compose up -d --build

3. После завершения процесса развертывания и запуска приложений в контейнерах docker  к приложению можно обращаться через http://localhost:8000/

4. В браузере по адресу http://localhost:8000/swagger/ можно ознакомиться с описанием API.



