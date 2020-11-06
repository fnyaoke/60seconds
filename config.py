import os
#from dotenv import load_dotenv
#load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI ='postgres://moringa:Access@localhost:5432/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY='18511174a077429aaaeaee76c5574ee9'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
     #pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}