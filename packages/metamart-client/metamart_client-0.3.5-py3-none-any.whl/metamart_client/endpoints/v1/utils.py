from uuid import uuid4

from metamart_schemas.v1.node import NodeIdTypes

from metamart_client.endpoints.client import ClientOptions
from metamart_client.endpoints.rest import get
from metamart_client.endpoints.v1.client import ClientV1


def process_node_id(client: ClientV1, metamart_type: NodeIdTypes, options: ClientOptions = ClientOptions()) -> NodeIdTypes:
    """Process a NodeID object, either by returning if it has a known id, or by getting
    the id from the server.

    Args:
        client (ClientV1):
        metamart_type (NodeIdTypes):
        options (ClientOptions, optional):  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    if metamart_type.id is not None:
        return metamart_type

    server_node = get(client, metamart_type, options=options)
    if server_node is None:
        if metamart_type.id is None:
            message = (
                f"Could not find node with namespace=`{metamart_type.namespace} " f"and name=`{metamart_type.name}` on server"
            )
        else:
            message = f"Could not find node with id=`{metamart_type.id}`"
        raise ValueError(message)

    return server_node.spec


class MockClientV1(ClientV1):
    """A mock client that can be used for testing."""

    def __init__(self, workspace=None, **kwargs):
        self._workspace = str(uuid4()) if workspace is None else workspace
        username = kwargs.get("username", "null@metamart.io")
        password = kwargs.get("password", "super_secret")
        url = kwargs.get("url", "http://localhost:8000")
        super().__init__(workspace=workspace, username=username, password=password, url=url, **kwargs)

    @property
    def workspace(self):
        return self._workspace

    def authenticate(*args, **kwargs) -> None:
        pass
