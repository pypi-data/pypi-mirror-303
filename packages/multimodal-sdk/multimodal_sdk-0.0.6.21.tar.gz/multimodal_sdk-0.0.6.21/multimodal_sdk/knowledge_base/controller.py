import aiohttp
import os
import logging
from multimodal_sdk.common.refresh import token_refresh_handler
from multimodal_sdk.common.http_status_handler import HTTPStatusHandler
from multimodal_sdk.common.decorators import log_and_authorize
from multimodal_sdk.common.retry_decorator import retry_on_client_error
from multimodal_sdk.knowledge_base.poll_task_status import PollTaskStatusNamespace

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@retry_on_client_error()
@token_refresh_handler
@log_and_authorize
@HTTPStatusHandler(201)
async def create_collection_func(
    kb_resource_id,
    collection_name,
    ingestion_strategy,
    distance_method=None,
    main_lang=None,
    chunk_strategy=None,
    embedding_strategy=None,
    **kwargs
):
    payload = {
        "name": collection_name,
        "ingestion_strategy": {
            "for_types": ingestion_strategy
        },
        "distance_method": distance_method if distance_method else "cosine",
        "main_lang": main_lang if main_lang else "ja",
        "chunk_strategy": chunk_strategy if chunk_strategy else {"active": True, "max_size": "auto"}
    }

    if embedding_strategy is not None:
        payload["embedding_strategy"] = embedding_strategy
    
    logger.info("KnowledgeBase: create_collection payload: %s", payload)
    
    url = f"{kwargs['base_url']}/knowledge-bases/{kb_resource_id}/collections"

    async with aiohttp.ClientSession() as session:
        return await session.post(url, json=payload, headers=kwargs['headers'])

@retry_on_client_error()
@token_refresh_handler
@log_and_authorize
@HTTPStatusHandler(204)
async def delete_collection_func(
    kb_resource_id,
    collection_name,
    **kwargs
):
    url = f"{kwargs['base_url']}/knowledge-bases/{kb_resource_id}/collections"
    payload = {
        "name": collection_name
    }

    async with aiohttp.ClientSession() as session:
        return await session.delete(url, json=payload, headers=kwargs['headers'])

@retry_on_client_error()
@token_refresh_handler
@log_and_authorize
@HTTPStatusHandler(200)
async def get_collection_func(
    kb_resource_id,
    **kwargs
):
    url = f"{kwargs['base_url']}/knowledge-bases/{kb_resource_id}/collections"

    async with aiohttp.ClientSession() as session:
        return await session.get(url, headers=kwargs['headers'])

@retry_on_client_error()
@token_refresh_handler
@log_and_authorize
@HTTPStatusHandler(201)
async def ingest_data_func(
    kb_resource_id,
    ingestion_type,
    texts=None,
    data=None,
    ids=None,
    **kwargs
):
    if isinstance(ingestion_type, str):
        ingestion_type = [ingestion_type]
    if isinstance(texts, str):
        texts = [texts]
    if isinstance(data, str):
        data = [data]
    if isinstance(ids, str):
        ids = [ids]

    texts, data, ids = texts or [], data or [], ids or []
    combined = texts + data

    if (ids and not (len(ingestion_type) == len(ids) == len(combined))) or (not ids and len(ingestion_type) != len(combined)):
        error_message = f"The length of ingestion_type and {'texts + data and ids' if ids else 'texts + data'} must be equal."
        logger.error(error_message)
        raise ValueError(error_message)

    url = f"{kwargs['base_url']}/knowledge-bases/{kb_resource_id}"
    logger.info(f"Endpoint URL: {url}")

    form_data = aiohttp.FormData()
    files_to_close = []

    try:
        for x, y, z in zip(ingestion_type, combined, ids) if ids else zip(ingestion_type, combined):
            form_data.add_field('ingestion_type', x)
            if ids:
                form_data.add_field('ids', z)
            if y in texts:
                form_data.add_field('texts', y)
            elif y in data and os.path.isfile(y):
                file = open(y, 'rb')
                form_data.add_field('data', file, filename=os.path.basename(y))
                files_to_close.append(file)
            elif y in data:
                error_message = f"File not found or not a valid file: {y}"
                logger.error(error_message)
                raise ValueError(error_message)

        logger.info("Form data created successfully")

        async with aiohttp.ClientSession() as session:
            return await session.post(url, data=form_data, headers=kwargs['headers'])
    finally:
        for file in files_to_close:
            file.close()
            logger.info(f"Closed file: {file.name}")

@retry_on_client_error()
@token_refresh_handler
@log_and_authorize
@HTTPStatusHandler([200, 202])
async def retrieve_data_func(
    kb_resource_id,
    query,
    threshold=0.7,
    limit=5,
    timeout=20,
    sync=False,
    history=[],
    inject="",
    **kwargs
):
    if not query or not query.strip():
        raise ValueError("Query is required and cannot be empty.")

    params = {
        "query": query,
        "threshold": threshold,
        "limit": limit,
        "inject": inject,
    }

    body = {}
    if history:
        body['msg_history'] = history

    url = f"{kwargs['base_url']}/knowledge-bases/{kb_resource_id}/rag"
    logger.info(f"Endpoint URL: {url}")

    logger.info("Query parameters:")
    for key, value in params.items():
        logger.info(f"{key}: {value}")

    if body:
        logger.info(f"Request body: {body}")

    async with aiohttp.ClientSession() as session:
        res = await session.post(url, headers=kwargs['headers'], params=params, json=body)
        if res.status != 401:
            result = await PollTaskStatusNamespace.poll_task_status_handler(
                res,
                status_url=f"http://192.168.1.27:5002/api/v1/tasks/status",
                task_id_key='task_id',
                headers=kwargs['headers']
            )
            return result
        return res

@retry_on_client_error()
@token_refresh_handler
@log_and_authorize
@HTTPStatusHandler([200, 202])
async def retrieve_data_func_beta(
    kb_resource_id,
    query,
    inject="",
    thread_id="",
    create_thread=False,
    history=[],
    **kwargs
):
    if not query or not query.strip():
        raise ValueError("Query is required and cannot be empty.")

    params = {
        "query": query,
        "inject": inject,
        "version": "beta",
    }

    body = {}
    if history:
        body['msg_history'] = history

    if create_thread:
        params['create_thread'] = create_thread
    if thread_id:
        params['thread_id'] = thread_id

    url = f"{kwargs['base_url']}/knowledge-bases/{kb_resource_id}/rag"
    logger.info(f"Endpoint URL: {url}")

    logger.info("Query parameters:")
    for key, value in params.items():
        logger.info(f"{key}: {value}")
    
    if body:
        logger.info(f"Request body: {body}")

    # async with aiohttp.ClientSession() as session:
    #     res = await session.post(url, headers=kwargs['headers'], params=params)
    #     return res
    
    async with aiohttp.ClientSession() as session:
        res = await session.post(url, headers=kwargs['headers'], params=params)
        if res.status != 401:
            result = await PollTaskStatusNamespace.poll_task_status_handler(
                res,
                status_url=f"http://192.168.1.27:5002/api/v1/tasks/status",
                task_id_key='task_id',
                headers=kwargs['headers']
            )
            return result
        return res

@retry_on_client_error()
@token_refresh_handler
@log_and_authorize
@HTTPStatusHandler([200, 202])
async def search_data_func(
    kb_resource_id,
    query,
    **kwargs
):
    if not query or not query.strip():
        raise ValueError("Query is required and cannot be empty.")

    params = {
        "query": query,
        "threshold": 0.7,
        "limit": 5,
        "includes": "distances",
        "sync": "true",
    }

    url = f"{kwargs['base_url']}/knowledge-bases/{kb_resource_id}/search"
    logger.info(f"Endpoint URL: {url}")

    logger.info("Query parameters:")
    for key, value in params.items():
        logger.info(f"{key}: {value}")

    async with aiohttp.ClientSession() as session:
        res = await session.get(url, headers=kwargs['headers'], params=params)
        return res

@retry_on_client_error()
@token_refresh_handler
@log_and_authorize
@HTTPStatusHandler(204)
async def delete_item_func(
    kb_resource_id,
    record_id,
    **kwargs
):
    res = await get_collection_func(kb_resource_id=kb_resource_id, **kwargs)

    if res["status"] == "success":
        collection_ids = []
        data = res.get("data", {})
        collections = data.get("collections", [])
        for collection in collections:
            collection_ids.append(collection.get("id"))
        
        logger.info(f"Collection IDs: {collection_ids}")
        logger.info(f"kwargs: {kwargs}, kb_resource_id: {kb_resource_id}")

        for collection_id in collection_ids:
            url = f"{kwargs['base_url']}/knowledge-bases/{kb_resource_id}/collections"
            payload = {
                "id": collection_id,
                "records_ids": [record_id]
            }

            async with aiohttp.ClientSession() as session:
                logger.info(f"Payload: {payload}")
                res_delete_item = await session.delete(url, json=payload, headers=kwargs['headers'])

                if res_delete_item.status == 204:
                    logger.info(f"Record with ID: {record_id} deleted successfully.")
                    return res_delete_item
                elif collection_id == collection_ids[-1]:
                    return res_delete_item
    else:
        return res

@retry_on_client_error()
@token_refresh_handler
@log_and_authorize
@HTTPStatusHandler(200)
async def get_ingested_chunks_func(
    kb_resource_id,
    record_id,
    **kwargs
):
    updated_record_id = f"{record_id}"
    # if ingestion_type == "pdf":
    #     if get_chunk_type is None:
    #         updated_record_id = f"{record_id}_script"
    #     else:
    #         updated_record_id = f"{record_id}_summary"
    params = {
        "record_id": updated_record_id,
        "sync": "true",
        "includes": "documents",
        "limit": 5
    }
    url = f"{kwargs['base_url']}/knowledge-bases/{kb_resource_id}/get"

    logger.info(f"Params: {params}")

    async with aiohttp.ClientSession() as session:
        return await session.get(url, headers=kwargs['headers'], params=params)