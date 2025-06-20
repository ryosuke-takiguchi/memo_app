class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://user:password@localhost:5432/memo_app"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your-secret-key"
