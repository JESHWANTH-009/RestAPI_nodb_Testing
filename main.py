from fastapi import FastAPI
from routers import task

from middleware.logger import FileLoggerMiddleware
from middleware.ratelimit import RateLimitMiddleware

app = FastAPI()

app.add_middleware(FileLoggerMiddleware)
#app.add_middleware(BlockIPMiddleware)
app.add_middleware(RateLimitMiddleware)


app.include_router(task.router, prefix="/api")
#app.include_router(auth.router, prefix="/api")
