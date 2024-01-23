# About
#### Monday 22 January 2024
## Front-End:
    - VueJS:
        Adopted an unconventional approach. Vue components isolate scheme.
## Back-End:
    - Flask:
        Used Flask-WTF for the validate type value. I don't like how it implements CSRF.
        Therefore, I implemented a UUID generator to tag each HTTP POST call.
    - Redis:
        Adopted from Redis the use of shared cache data.
        In this way, I can have a vault for UUID shared on a server like Gunicorn or Asynchrony.
[![](https://mermaid.ink/img/pako:eNptkMFqwzAMhl_F6LrkBXwodLSB7djQnAxF2GpjktitLTNGyLvPbstYynwy0vdJvz2D9oZAQqRbIqdpZ_EScFJO5NMl-mxPTfCOyZl6s3lrRozD6R31kAtSNMS6F4fiRhZflntxPH7sHvaKLfKBjI1SdDhag0x_0Hunzkz9sqAgv4L5b26R1jml2CbuybHVyNY70SatKcZzGqGCicKE1uQnz2WcgoxOpEDmq8EwKFBuyRwm9u230yA5JKogXUuE5_esi3tj2QeQZxwjLT_bOHN1?type=png)](https://mermaid.live/edit#pako:eNptkMFqwzAMhl_F6LrkBXwodLSB7djQnAxF2GpjktitLTNGyLvPbstYynwy0vdJvz2D9oZAQqRbIqdpZ_EScFJO5NMl-mxPTfCOyZl6s3lrRozD6R31kAtSNMS6F4fiRhZflntxPH7sHvaKLfKBjI1SdDhag0x_0Hunzkz9sqAgv4L5b26R1jml2CbuybHVyNY70SatKcZzGqGCicKE1uQnz2WcgoxOpEDmq8EwKFBuyRwm9u230yA5JKogXUuE5_esi3tj2QeQZxwjLT_bOHN1)
