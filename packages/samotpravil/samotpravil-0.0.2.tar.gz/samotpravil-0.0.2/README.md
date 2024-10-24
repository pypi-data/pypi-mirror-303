# Sam Optravil

Python библиотека для сервиса Sam Optravil.

[Официальный сайт](https://samotpravil.ru/)

[Подробная документация REST API](https://documentation.samotpravil.ru/view/26779685/2s93RZM9in)

Библиотека является оберткой для API методов

## Установка

```bash
pip install samotpravil
```

## Начало работы

```python
from samotpravil import SamotpravilClient

# Инициализация
service = SamotpravilClient('*****************')
```
Запросите доступы, [заполнив форму](https://samotpravil.ru/get-access).

## Методы
Отправить письмо. [Описание в API документации](https://documentation.samotpravil.ru/#15015693-d4bd-4b55-a319-e8402d96d062)
```python
service.send_email(email_to='email@example.com',
                   subject='Hello from library',
                   message_text='Hello world',
                   email_from='info@samotpravil.ru')
```

### Обязательные поля
- `email_to` - имейл получателя (str)
- `subject` - тема письма (str)
- `message_text` - текст письма с поддержкой HTML (str)
- `email_from` - имейл отправителя (str)
### Необязательные поля
- `params` - массив собственных переменных (dict)
- `x_track_id` - ваш уникальный ID отправки (str)
- `track_open` - отслеживать открытия (bool)
- `track_click` - отслеживать клики (bool)
- `track_domain` - домен трекинга (str)
- `check_stop_list` - проверять по глобальному стоп-листу (bool)
- `check_local_stop_list` - проверять по клиентскому стоп-листу (bool)
- `domain_for_dkim` - домен для DKIM
- `headers` - свои заголовки (dict)




---
Получить статус доставки. [Описание в API документации](https://documentation.samotpravil.ru/#0cee65d5-4fe3-4efb-916a-23759269bfc7)
```python
service.get_status(message_id='1qBv3w-0007Ls-CS11')
```
### Обязательные поля
- `message_id` - уникальный ID отправки системы (str)

или
- `x_track_id` - ваш ID отправки системы (str)





---
Получить статистику. [Описание в API документации](https://documentation.samotpravil.ru/#8a425ab8-8cbc-4c35-9242-16deb884d634)
```python
service.get_statistics(date_from='2024-10-01',
                       date_to='2024-10-31')
```
### Обязательные поля
- `date_from` - дата в формате YYYY-MM-DD (str)
- `date_to` - дата в формате YYYY-MM-DD (str)
### Необязательные поля
- `limit` - лимит объектов в ответе, дефолт - 100 (int)
- `cursor_next` - пагинация (int)




---
Получить отчет о недоставках за период. [Описание в API документации](https://documentation.samotpravil.ru/#f7a7690a-ad7c-4cc0-ac03-301200259199)
```python
service.get_non_delivery_by_date(date_from='2024-10-01',
                                 date_to='2024-10-31')
```
### Обязательные поля
- `date_from` - дата в формате YYYY-MM-DD (str)
- `date_to` - дата в формате YYYY-MM-DD (str)
### Необязательные поля
- `limit` - лимит объектов в ответе, дефолт - 100 (int)
- `cursor_next` - пагинация (int)



---
Получить отчет о недоставках по номеру выпуска. [Описание в API документации](https://documentation.samotpravil.ru/#01de9691-fe9d-47aa-b00b-35c97091ea5a)
```python
service.get_non_delivery_by_issue(issuen=12345)
```
### Обязательные поля
- `issuen` - ID выпуска (int)



---
Получить отчет о жалобах за период. [Описание в API документации](https://documentation.samotpravil.ru/#49ddff28-6b93-48fa-a7fc-0fbd63a73791)
```python
service.get_fbl_report_by_date(date_from='2024-10-01',
                               date_to='2024-10-31')
```
### Обязательные поля
- `date_from` - дата в формате YYYY-MM-DD (str)
- `date_to` - дата в формате YYYY-MM-DD (str)
### Необязательные поля
- `limit` - лимит объектов в ответе, дефолт - 100 (int)
- `cursor_next` - пагинация (int)




---
Получить отчет о жалобах по номеру выпуска. [Описание в API документации](https://documentation.samotpravil.ru/#9b28ba17-7fd4-4e80-b647-c9baf9d2d979)
```python
service.get_fbl_report_by_issue(issuen=12345)
```
### Обязательные поля
- `issuen` - ID выпуска (int)



---
Искать имейл в стоп-листе. [Описание в API документации](https://documentation.samotpravil.ru/#56ba4dd4-2f5a-4764-9b5c-434d76bcfc2d)
```python
service.stop_list_search(email='example@mail.com')
```
### Обязательные поля
- `email` - имейл, который нужно найти (str)



---
Добавить имейл в стоп-лист. [Описание в API документации](https://documentation.samotpravil.ru/#cf6dbfae-04e1-4fcf-847e-2c977a4db3b5)
```python
service.stop_list_add(email='example@mail.com',
                      domain='samotpravil.ru')
```
### Обязательные поля
- `email` - имейл, который нужно добавить (str)
- `domain` - домен, для которого нужно добавить в стоп-лист (str)



---
Удалить имейл из стоп-листа. [Описание в API документации](https://documentation.samotpravil.ru/#e3357191-6c9f-4bb7-9651-e99cb63dc8bb)
```python
service.stop_list_remove(email='example@mail.com',
                         domain='samotpravil.ru')
```
### Обязательные поля
- `email` - имейл, который нужно удалить (str)
- `domain` - домен, для которого нужно удалить имейл из стоп-листа (str)





---
Получить список разрешенных доменов. [Описание в API документации](https://documentation.samotpravil.ru/#def0eb00-3660-4713-8bfe-accd2efc89b6)
```python
service.get_domains()
```


---
Добавить домен в разрешенные. [Описание в API документации](https://documentation.samotpravil.ru/#372d5d44-eb09-4eda-8895-3dedc2fde511)
```python
service.domain_add(domain='samotpravil.ru')
```
### Обязательные поля
- `domain` - домен, который нужно добавить (str)



---
Удалить домен из разрешенных. [Описание в API документации](https://documentation.samotpravil.ru/#9a51577c-4e58-4ec7-aef1-53d5530d66aa)
```python
service.domain_remove(domain='samotpravil.ru')
```
### Обязательные поля
- `domain` - домен, который нужно удалить (str)


---
Проверить верификацию домена. [Описание в API документации](https://documentation.samotpravil.ru/#ddb3a718-c74e-41ce-ae8f-77e2ff585b1a)
```python
service.domain_check_verification(domain='samotpravil.ru')
```
### Обязательные поля
- `domain` - домен, который нужно проверить (str)
