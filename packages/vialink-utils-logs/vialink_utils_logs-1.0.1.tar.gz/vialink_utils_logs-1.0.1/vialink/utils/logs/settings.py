from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str = 'dev'

    AWS_REGION: str = 'ap-southeast-1'


settings = Settings()
