import json
import os
import redis.asyncio as redis
from typing import Optional

class LicenseManager:
    def __init__(self, redis_client: redis.Redis):
        """Redis クライアントの初期化"""
        self.redis_client = redis_client

    async def check_connection(self):
        """Redisへの接続テスト"""
        try:
            is_connected = await self.redis_client.ping()
            if is_connected:
                print("Redis connection successful")
                return {"status": "success", "message": "Redis connection successful"}
            else:
                raise ValueError("Redis ping failed")
        except redis.ConnectionError as e:  # 修正点
            raise ValueError(f"Redis connection failed: {str(e)}")
        except Exception as e:
            raise ValueError(f"Unexpected error: {str(e)}")

    async def validate_api_key(self, api_key: str) -> Optional[dict]:
        """APIキーの検証"""
        try:
            user_info_json = await self.redis_client.get(api_key)
            if not user_info_json:
                raise ValueError("Invalid API key.")
            return json.loads(user_info_json)
        except redis.ConnectionError as e:  # 修正点
            raise ValueError(f"Redis connection error: {str(e)}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to decode JSON: {str(e)}")
        except Exception as e:
            raise ValueError(f"Unexpected error: {str(e)}")

    async def add_license(self, api_key: str, user_info: dict):
        """ライセンスの追加"""
        try:
            if await self.redis_client.get(api_key):
                raise ValueError("API key already exists.")
            await self.redis_client.set(api_key, json.dumps(user_info))
        except redis.ConnectionError as e:  # 修正点
            raise ValueError(f"Redis connection error: {str(e)}")
        except Exception as e:
            raise ValueError(f"Failed to add license: {str(e)}")

    async def remove_license(self, api_key: str):
        """ライセンスの削除"""
        try:
            await self.redis_client.delete(api_key)
        except redis.ConnectionError as e:  # 修正点
            raise ValueError(f"Redis connection error: {str(e)}")
        except Exception as e:
            raise ValueError(f"Failed to remove license: {str(e)}")
