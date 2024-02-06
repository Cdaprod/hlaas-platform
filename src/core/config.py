from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "HLaaS Platform API Gateway"
    admin_email: str = "admin@example.com"
    # Add more configuration variables as needed

settings = Settings()