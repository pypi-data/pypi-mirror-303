from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = 'dev'

    AWS_REGION: str = 'ap-southeast-1'
    AWS_SNS_KEY: str = None
    AWS_SNS_SECRET: str = None
    AWS_SNS_PATH: str = 'arn:aws:sns:ap-southeast-1:580482583062:'


settings = Settings()
