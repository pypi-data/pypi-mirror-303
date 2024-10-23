from fastapi import HTTPException, status
from typing import Dict
import time
import redis.asyncio as redis

class RateLimiter:
    def __init__(self, free_calls: int = 5, period: int = 3600, redis_client: redis.Redis = None):
        self.free_calls = free_calls
        self.period = period
        self.redis_client = redis_client

    async def enforce_limit(self, user: Dict, ip: str):
        """Apply rate limit based on the user plan."""
        if user["plan"] == "paid":
            print(f"User plan: {user['plan']} - Unlimited access")
            return

        key = f"rate_limit:{ip}"
        current_time = int(time.time())

        try:
            count = await self.redis_client.incr(key)
            print(f"IP: {ip} - Current Count: {count}")

            if count == 1:
                await self.redis_client.expire(key, self.period)
                print(f"TTL set to {self.period} seconds for IP: {ip}")

            if count > self.free_calls:
                print(f"Rate limit exceeded for IP: {ip}")
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Rate limit exceeded. Try again later."
                )
        except redis.exceptions.ConnectionError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Rate limiter connection error: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Unexpected error: {str(e)}"
            )
