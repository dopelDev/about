# About
#### Monday 22 January 2024
![img](https://github.com/dopelDev/about/blob/main/img/DALL%C2%B7E%202024-01-22%2018.40.38%20-%20Un%20hombre%20del%20Mediterr%C3%A1neo%20mirando%20hacia%20un%20espejo%20grande%20y%20elegante%20para%20hacer%20un%20autoretrato%2C%20en%20un%20estilo%20futurista%20steampunk.%20La%20escena%20se%20desarro.png)
## Front-End:
    - VueJS:
        Adopted an unconventional approach. Vue components isolate scheme.
## Back-End:
    - Flask:
        Used Flask-WTF for the validate type value. I don't like how it implements CSRF. Therefore, I implemented a UUID generator to tag each HTTP POST call.
    - Redis:
        Adopted from Redis the use of shared cache data. In this way, I can have a vault for UUID shared on a server like Gunicorn or Asynchrony.
