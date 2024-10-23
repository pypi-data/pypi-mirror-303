from fastapi import FastAPI
from vault_service.routers.routes import router


app = FastAPI()

# Include the router with all routes
app.include_router(router)
