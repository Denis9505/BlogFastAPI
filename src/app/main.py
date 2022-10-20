from fastapi import FastAPI
import uvicorn

from settings import settings
from routes import routes as post_router
from api.auth import router as auth_roter


app = FastAPI()


app.include_router(post_router)
app.include_router(auth_roter)


if __name__ == "__main__":
    uvicorn.run(
    'main:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
