from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

class FileLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        end = time.time()

        log = f"{request.client.host} - {request.method} {request.url.path} - {response.status_code} - {end - start:.4f}s\n"
        with open("logs.txt", "a") as log_file:
            log_file.write(log)
        return response