from fastapi import FastAPI

try:
    from backend.main import app as backend_app

    app = backend_app
except Exception as exc:  # pragma: no cover
    app = FastAPI(title="Startup Ecosystem Backend (Fallback)")

    @app.get("/")
    def root():
        return {
            "status": "fallback",
            "message": "Backend import failed.",
            "error": str(exc),
        }

    @app.get("/health")
    def health():
        return {
            "status": "fallback",
            "message": "Backend import failed.",
            "error": str(exc),
        }
