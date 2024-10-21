import logging
import asyncio
from multimodal_sdk.common.base import BaseMultiModalRag
from multimodal_sdk.tenant.abstract_class import AbstractTenantHandler
from multimodal_sdk.tenant.controller import (
    create_tenant_func,
    delete_tenant_func,
    get_tenant_func,
    create_knowledge_base_func,
    delete_knowledge_base_func,
    get_knowledge_base_func
)
from multimodal_sdk.knowledge_base import KnowledgeBase
from multimodal_sdk.user_handler import UserHandler
from multimodal_sdk.role.main import _Role

import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Tenant(BaseMultiModalRag, AbstractTenantHandler, _Role):
    def __init__(self, oauth_url=None, base_url=None, authz_url=None):
        super().__init__(base_url=base_url)
        self.oauth_url = oauth_url if oauth_url else self.oauth_url
        self.authz_url = authz_url if authz_url else self.authz_url

        _Role.__init__(self, tenant=self)

    def _inject_params(func):
        async def wrapper(self, *args, **kwargs):
            access_token = kwargs.get('access_token')
            refresh_token = kwargs.get('refresh_token')
            if not access_token or not refresh_token:
                raise ValueError("access_token and refresh_token are required.")

            kwargs['oauth_url'] = self.oauth_url
            kwargs['base_url'] = self.base_url
            kwargs['authz_url'] = self.authz_url

            return await func(self, *args, **kwargs)
        return wrapper
    
    @staticmethod
    def get_tenant_id(response):
        tenant_id = response.get("data", {}).get("tenant", {}).get("id", "")
        if tenant_id:
            return tenant_id
        else:
            raise ValueError("Tenant ID not found in the response.")

    @_inject_params
    async def create_tenant(self, tenant_name: str, **kwargs):
        logger.info("Calling create_tenant with tenant_name: %s, kwargs: %s", tenant_name, kwargs)
        result = await create_tenant_func(
            tenant_name=tenant_name,
            **kwargs
        )

        logger.info("Tenant: create_tenant response: %s", result)
        return result

    @_inject_params
    async def delete_tenant(self, tenant_name: str, **kwargs):
        result = await delete_tenant_func(
            tenant_name=tenant_name,
            **kwargs
        )

        logger.info("Tenant: delete_tenant response: %s", result)
        return result

    @_inject_params
    async def get_tenant(self, **kwargs):
        result = await get_tenant_func(
            **kwargs
        )

        logger.info("Tenant: get_tenant response: %s", result)
        return result

    @_inject_params
    async def create_knowledge_base(self, tenant_resource_id: str, kb_name: str, **kwargs):
        result = await create_knowledge_base_func(
            tenant_resource_id=tenant_resource_id,
            kb_name=kb_name,
            **kwargs
        )

        logger.info("Tenant: create_knowledge_base response: %s", result)
        return result

    @_inject_params
    async def delete_knowledge_base(self, tenant_resource_id: str, kb_name: str, **kwargs):
        result = await delete_knowledge_base_func(
            tenant_resource_id=tenant_resource_id,
            kb_name=kb_name,
            **kwargs
        )

        logger.info("Tenant: delete_knowledge_base response: %s", result)
        return result

    @_inject_params
    async def get_knowledge_base(self, tenant_resource_id: str, **kwargs):
        result = await get_knowledge_base_func(
            tenant_resource_id=tenant_resource_id,
            **kwargs
        )

        logger.info("Tenant: get_knowledge_base response: %s", result)
        return result

async def main():
    logger.info("Testing Tenant class")
    logger.info("Creating Tenant object")

    t = Tenant()
    kb = KnowledgeBase()

    # Users : toyo_test_user_123, toyo_test_user_321, toyo_test_user_456

    # User Handler
    user_handler = UserHandler()

    login_user = await user_handler.login(
        username="masoomraj_mw",
        # username="mwtoyo_2312",
        password="Tokyo@6377300390"
    )
    logger.info("login_user final response (mwtoyo_2312): %s", login_user)

    access_token_123 = UserHandler.get_access_token(login_user)
    refresh_token_123 = UserHandler.get_refresh_token(login_user)

    # Ingest Data
    # response = await kb.ingest_data(
    #     kb_resource_id="21d30808-6f00-43bc-baeb-9233d95a5fc6",
    #     ingestion_type="text",
    #     texts="Hi there, I need some help",
    #     ids="123-123-123-1233",
    #     access_token=access_token_123,
    #     refresh_token=refresh_token_123
    # )
    # logger.info("(TEST) ingest_data response: %s", response)

    # Retrieve data
    response = await kb.retrieve_data(
        kb_resource_id="0e017ade-d094-4c99-847f-fde1cfd5c6a4",
        query="Hi there, I need some help",
        access_token=access_token_123,
        refresh_token=refresh_token_123,
        rag_version="beta",
        thread_id="a1234",
    )
    logger.info("retrieve_data response: %s", response)


    response = await kb.retrieve_data(
        kb_resource_id="0e017ade-d094-4c99-847f-fde1cfd5c6a4",
        query="Hi there, I need some help",
        access_token=access_token_123,
        refresh_token=refresh_token_123,
        rag_version="beta",
        thread_id="a1234",
        create_thread="true",
    )
    logger.info("retrieve_data response: %s", response)

    # Delete item
    # response = await kb.delete_item(
    #     kb_resource_id="21d30808-6f00-43bc-baeb-9233d95a5fc6",
    #     record_id="123-123-123-1233",
    #     access_token=access_token_123,
    #     refresh_token=refresh_token_123
    # )
    # logger.info("(TEST) delete_item response: %s", response)

    # Search Data
    # response = await kb.search_data(
    #     kb_resource_id="ec790cc2-3972-4d8e-a474-3b0010e83455",
    #     query="What does ingestor role means ?",
    #     access_token=access_token_123,
    #     refresh_token=refresh_token_123
    # )
    # logger.info("(TEST) search_data response: %s", response)




if __name__ == "__main__":
    asyncio.run(main())
