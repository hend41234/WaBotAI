from fastapi import FastAPI
from app.api import app_router

#-> init app ------------------------------------------
app = FastAPI(
    title="Whatsapp Bot",
    version="0.0.1"
)


#-> include router -----------------------------------
app.include_router(app_router)
