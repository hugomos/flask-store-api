class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/flask_migrate"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
