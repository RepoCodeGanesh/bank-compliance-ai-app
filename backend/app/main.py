import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.core.config import settings

# Configure Azure Monitor OpenTelemetry if connection string is present
try:
    from azure.monitor.opentelemetry import configure_azure_monitor
    if settings.APPLICATIONINSIGHTS_CONNECTION_STRING:
        configure_azure_monitor()
except Exception as e:
    logging.getLogger(__name__).debug("OpenTelemetry init skipped: %s", e)

app = FastAPI(
    title="BankCompliance AI API",
    description="Cloud-Native Banking Regulatory & Compliance Copilot API",
    version="1.0.0"
)

# ALLOWED_ORIGINS is injected via k8s ConfigMap (bankc-backend-config).
# It is a comma-separated string, e.g. "https://bank.mytaxbot.site"
# Combining allow_origins=["*"] with allow_credentials=True violates the
# Fetch spec and is rejected by all browsers — always use an explicit list.
_allowed_origins = [o.strip() for o in settings.ALLOWED_ORIGINS.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/healthz", tags=["Health"])
async def healthz():
    return {"status": "healthy", "service": "bank-compliance-backend", "version": "1.0.0"}
