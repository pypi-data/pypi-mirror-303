import os

from wwai_sdk.wwai_client import WwaiClient


def create_client(
        grant_type=None,
        server=None,
        authorization: str = None,
        username=None,
        password=None,
        tenant_code=None,
        client_id=None,
        client_secret=None,
        cache_type=None,
        redis_host=None,
        redis_port=6379,
        redis_password=None,
        redis_db=0,
        rsa_private_key=None,
):
    if not grant_type:
        grant_type = os.getenv("WWAI_GRANT_TYPE", grant_type)
    if not server:
        server = os.getenv("WWAI_SERVER", server)
    if not server:
        server = "http://ai.api.wwai.wwxckj.com"
    if not authorization:
        authorization = os.getenv("WWAI_AUTHORIZATION", authorization)
    if not username:
        username = os.getenv("WWAI_USERNAME", username)
    if not password:
        password = os.getenv("WWAI_PASSWORD", password)
    if not tenant_code:
        tenant_code = os.getenv("WWAI_TENANT_CODE", tenant_code)
    if not client_id:
        client_id = os.getenv("WWAI_CLIENT_ID", client_id)
    if not client_secret:
        client_secret = os.getenv("WWAI_CLIENT_SECRET", client_secret)
    if not cache_type:
        cache_type = os.getenv("WWAI_CACHE_TYPE", cache_type)
    if not redis_host:
        redis_host = os.getenv("REDIS_HOST", redis_host)
    if not redis_port:
        redis_port = os.getenv("REDIS_PORT", redis_port)
    if not redis_password:
        redis_password = os.getenv("REDIS_PASSWORD", redis_password)
    if not redis_db:
        redis_db = os.getenv("REDIS_DB", redis_db)
    if not rsa_private_key:
        rsa_private_key = os.getenv("WWAI_RSA_PRIVATE_KEY", rsa_private_key)

    if grant_type == "password":
        authorization = 'Basic d3dhaTptem5lc2hhaXlxam94dGRmdXJwd2NrZ3ZibG5icmt1cQ=='
    if authorization is not None and authorization != "" and not authorization.startswith("Basic "):
        authorization = "Basic " + authorization

    client = WwaiClient(
        grant_type=grant_type,
        server=server,
        authorization=authorization,
        username=username,
        password=password,
        tenant_code=tenant_code,
        client_id=client_id,
        client_secret=client_secret,
        cache_type=cache_type,
        redis_host=redis_host,
        redis_port=redis_port,
        redis_password=redis_password,
        redis_db=redis_db,
        rsa_private_key=rsa_private_key
    )
    return client
