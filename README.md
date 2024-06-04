# Добрый день. Рад приветствовать тебя! 
- Этот сервис позволяет рассчитывать квартплату за квартиру или весь дом.

### Для начала работы с сервисом - склонируй репозиторий себе на компьютер.

```
git clone https://github.com/h-inek/yamdb_final.git
```

В директории есть необходимо создать файл .env и заполнить его в соответствии с .env.example.


Не забудь создать суперюзера
```
python manage.py createsuperuser
```
Так же потребуется загрузка создание миграций, для этого выполни команды:

```
python manage.py makemigrations
python manage.py migrate
python manage.py migrate django_celery_results

```


Автор:

Максим Кавтырев - https://github.com/h-inek


### Функционал подготовлен для работы с PostgreSQL.

### Используемые технологии
Python 3.9 Django 5.0.6 REST Framework 3.15.1 PostgreSQL 12.2 Celery 5.4.0 подробнее см. прилагаемый файл зависимостей requrements.txt
