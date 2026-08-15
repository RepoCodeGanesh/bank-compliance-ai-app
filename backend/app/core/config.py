from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings â€” pydantic-settings reads env vars automatically.
    Do NOT use os.getenv() inside this class; set field defaults instead.
    Values are injected at runtime via the k8s ConfigMap (bankc-backend-config).
    """
    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    APP_NAME: str = "BankCompliance AI"
    ENVIRONMENT: str = "production"

    # AI Gateway / LiteLLM Proxy
    LITELLM_URL: str = "http://litellm:4000/v1"
    OPENAI_MODEL: str = "gpt-5.4-nano"

    # Qdrant Vector DB
    QDRANT_HOST: str = "qdrant"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "rbi_master_directions"

    # Azure AI Content Safety (populated from Terraform output via k8s ConfigMap)
    CONTENT_SAFETY_ENDPOINT: str = ""

    # CORS â€” comma-separated allowed origins (injected by k8s ConfigMap)
    ALLOWED_ORIGINS: str = "https://happy-coast-00666250f.7.azurestaticapps.net,https://bank.mytaxbot.site,http://localhost:3000"

    # Azure Monitor OpenTelemetry (injected by k8s ConfigMap)
    APPLICATIONINSIGHTS_CONNECTION_STRING: str = ""

settings = Settings()

