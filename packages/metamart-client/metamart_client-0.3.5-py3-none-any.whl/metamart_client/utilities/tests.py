import os


def get_test_client():
    """ """
    from metamart_client.endpoints.v1.client import ClientV1

    host = os.environ.get("METAMART_HOST", "localhost")
    port = os.environ.get("METAMART_PORT", "8000")
    username = os.environ.get("METAMART_USERNAME", "null@metamart.io")
    password = os.environ.get("METAMART_PASSWORD", "super_secret")
    workspace = os.environ.get("METAMART_WORKSPACE", "default")

    client = ClientV1(host, port, workspace=workspace, insecure=True, username=username, password=password)

    return client
