from fastapi import Request,HTTPException ## Request is to access client IP and request data
from starlette.middleware.base import BaseHTTPMiddleware ## base class to create custom middleware
import time
from idlelib.debugobj import dispatch
from pip._vendor.requests.api import request
from anyio._core._eventloop import current_time

RATE_LIMIT=2
WINDOW_SECONDS=60

request_counts={}
class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request:Request,call_next):
        
        if request.url.path in ["/docs", "/openapi.json", "/redoc"]:
            return await call_next(request)
        
        ip=request.client.host
        current_time=time.time()
        if ip not in request_counts:
            request_counts[ip]=[]
        

        # Remove timestamps older than the time window
        request_counts[ip] = [t for t in request_counts[ip] if current_time - t < WINDOW_SECONDS]

        # If too many requests, block the request
        if len(request_counts[ip]) >= RATE_LIMIT:
            raise HTTPException(status_code=429, detail="Too many requests. Please try again later.")

        # Otherwise, add the timestamp and proceed
        request_counts[ip].append(current_time)
        return await call_next(request)
