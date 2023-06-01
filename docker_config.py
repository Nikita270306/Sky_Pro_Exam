class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://examen:examen_password@pg/examen_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False