# About
#### Monday 22 January 2024
## Front-End:
    - VueJS:
        Adopted an unconventional approach. Vue components isolate scheme.

![front](https://github.com/dopelDev/about/blob/main/Screenshot_2024-01-22_19-49-25.png)

## Back-End:
    - Flask:
        Used Flask-WTF for the validate type value. I don't like how it implements CSRF.
        Therefore, I implemented a UUID generator to tag each HTTP POST call.
    - Redis:
        Adopted from Redis the use of shared cache data.
        In this way, I can have a vault for UUID shared on a server like Gunicorn or Asynchrony.
        
![scheme](https://github.com/dopelDev/about/blob/main/diagrama.png)
