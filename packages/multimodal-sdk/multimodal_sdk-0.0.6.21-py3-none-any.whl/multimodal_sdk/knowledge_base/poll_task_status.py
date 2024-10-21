import logging
import aiohttp
import asyncio

logger = logging.getLogger(__name__)

class PollTaskStatusNamespace:
    @staticmethod
    async def poll_task_status_handler(response, status_url, task_id_key, headers, success_status_code=200, polling_interval=0.5, max_retries=100):
        try:
            response_json = await response.json()
            logger.info("Initial response: %s", response_json)
        except aiohttp.ContentTypeError:
            response_text = await response.text()
            logger.error("Non-JSON response received: %s", response_text)
            raise ValueError("Failed to process the response JSON.")

        task_id = response_json.get(task_id_key)
        if not task_id:
            raise ValueError("Response does not contain a valid task_id.")
        
        status_params = {"ids[]": task_id}

        async with aiohttp.ClientSession() as session:
            retries = 0
            while retries < max_retries:
                logger.info(f"Polling task status with task_id: {task_id}")
                status_res = await session.get(status_url, headers=headers, params=status_params)

                logger.info("Status response status code: %s", status_res.status)

                try:
                    status_res_json = await status_res.json()
                    logger.info("Status response: %s", status_res_json)
                except aiohttp.ContentTypeError:
                    status_res_text = await status_res.text()
                    logger.error("Non-JSON response received during polling: %s", status_res_text)
                    raise ValueError("Failed to process the status response JSON.")

                if status_res.status == success_status_code:
                    logger.info("Task completed successfully.")
                    return status_res
                
                if status_res.status == 500:
                    logger.error(f"Server error occurred during polling for task_id {task_id}: {status_res.status}")
                    raise RuntimeError(f"Server error (500) encountered for task_id {task_id}.")

                retries += 1
                await asyncio.sleep(polling_interval)

            raise TimeoutError(f"Max retries exceeded: {max_retries} attempts made without success.")
