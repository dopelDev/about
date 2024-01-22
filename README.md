# About
#### Monday 22 January 2024
![img](img/DALL·E 2024-01-22 18.40.38 - Un hombre del Mediterráneo mirando hacia un espejo grande y elegante para hacer un autoretrato, en un estilo futurista steampunk. La escena se desarro.png)
## Front-End:
    - VueJS:
        Adopted an unconventional approach. Vue components isolate scheme.
## Back-End:
    - Flask:
        Used Flask-WTF for the validate type value. I don't like how it implements CSRF. Therefore, I implemented a UUID generator to tag each HTTP POST call.
    - Redis:
        Adopted from Redis the use of shared cache data. In this way, I can have a vault for UUID shared on a server like Gunicorn or Asynchrony.
