# feodal-test-work
Було створено простий веб-додаток для управління списком завдань (ToDo) відповідно до тестового завдання.
Для реалізації серверної частини використано Django, DRF, для бази даних вибрана стандартна sqllite.
Для перевірки відправлень емейл повідомлень додайте до файлу app\settings.py наступні налаштування:
  - EMAIL_HOST_USER = "ваш акаунт гугл"
  - EMAIL_HOST_PASSWORD = "пароль від нього"
Щоб все спрацювало https://myaccount.google.com/u/0/lesssecureapps дозвольте доступ для ненадійних додатків.
Потім встановіть docker-compose якщо він у вас не встановлений вілповільно до операційної системм https://docs.docker.com/compose/install/.
Для запуску проекту локально використайте:
 docker-compose up --build
