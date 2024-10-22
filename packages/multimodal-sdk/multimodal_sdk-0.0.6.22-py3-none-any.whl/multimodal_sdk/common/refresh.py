import aiohttp
import logging
from functools import wraps

logger = logging.getLogger(__name__)

async def refresh_token(oauth_url, refresh_token):
    url = f"{oauth_url}/refresh"
    headers = {
        'Authorization': f'Bearer {refresh_token}'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers) as response:
            try:
                response_json = await response.json()
                logger.info(f"Response status: {response.status}, json: {response_json}")
            except aiohttp.ContentTypeError:
                response_text = await response.text()
                logger.error("Non-JSON response received during token refresh: %s", response_text)
                return None

            if response.status == 201:
                logger.info("Token refreshed successfully")
                return response_json.get("access_token")
            elif response.status == 401:
                logger.error("Invalid refresh token")
                return None
            else:
                logger.error("Unexpected error during token refresh")
                return None

def token_refresh_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        response = await func(*args, **kwargs)
        new_access_token = None

        # logger.info(f"Response in token_refresh_handler: {response}")
        if response.get('status_code') != 401:
            return response

        if response['status'] == 'error':
            data = response.get('data', {})
            if "Token has expired" in data.get("msg", ""):
                new_access_token = await refresh_token(kwargs['oauth_url'], kwargs['refresh_token'])
                if new_access_token:
                    kwargs['access_token'] = new_access_token
                    # Retry the request with the new access token
                    response = await func(*args, **kwargs)
                    response['new_access_token'] = new_access_token
        
        return response
    return wrapper
