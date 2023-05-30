from fastapi import FastAPI
from routes.lovebox import router as LoveBoxRouter
from utils.display_writer import DisplayWriter

app = FastAPI(
    title="LoveBox API",
    description="API for uploading text or images to the love box e-ink display",
    docs_url="/lovebox/docs",
    openapi_url="/lovebox/docs/openapi.json",
)

app.include_router(LoveBoxRouter, tags=["LoveBox"], prefix="/lovebox")


@app.get("/lovebox/healthz", tags=["Health"])
async def health():
    return "Healthy"
