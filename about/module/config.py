class Config():
    SECRET_KEY = 'sXAPgFDBuMxdavc4mHYRK3f97nwq8TkLGzJtr25WeU'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = '322kuroneko2@gmail.com'
    MAIL_PASSWORD = 'uwxf ckdz mxwi ywyd'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False

