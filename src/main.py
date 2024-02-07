import uvicorn

from src.config import config

uvicorn.run(
    "api:app",
    host="0.0.0.0",
    port=config.api.port,
    use_colors=True,
    log_level="warning"
)
