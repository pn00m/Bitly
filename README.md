# Обрезка ссылок с помощью сервиса Bitly

Утилита для обрезки ссылок при помощи сервиса Bitly, а также просмотра статистики по переходам по укороченным ссылкам.


### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для работы с данной утилитой Вам будет нужно 
- зарегистрироваться на сервисе Bitly по [ссылке](https://bitly.com/a/sign_up)
- получить токен по [ссылке](https://bitly.com/a/oauth_apps).    

Токен будет представлять собой строку типа `17c09e20ad155405123ac1977542fecf00231da7`  
Далее Вам нужно будет создать файл .env в корневой папке проекта и записать в него строку типа
BITLY_TOKEN=ваш токен

### Как использовать

Используйте следующий формат
```
python main.py ссылка
```
Входная ссылка принимается только в полном виде.  
Если в качестве входной ссылки используется уже сокращенный ранее адрес, то результатом работы программы является статистика по переходам по этой сокращенной ссылке.
В иных случаях результатом работы утилиты будет выдача обрезанной ссылки.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).