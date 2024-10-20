from typing import Optional, TypeVar, Union

from metamart_schemas.v1.edge import EdgeSpec, EdgeV1, SourcedEdgeSpec, SourcedEdgeV1
from metamart_schemas.v1.node import NodeSpec, NodeV1, SourcedNodeSpec, SourcedNodeV1
from metamart_schemas.v1.organization import OrganisationSpec, OrganisationV1
from metamart_schemas.v1.source import SourceSpec, SourceV1
from metamart_schemas.v1.workspace import WorkspaceSpec, WorkspaceV1

from metamart_client.endpoints.client import ClientOptions
from metamart_client.endpoints.rest import get, patch
from metamart_client.endpoints.v1.client import ClientV1
from metamart_client.endpoints.v1.get.utils import get_source_and_spec
from metamart_client.errors import NotSupportedError

T = TypeVar("T", NodeV1, EdgeV1)


@patch.register
def patch_node_v1(client: ClientV1, metamart_type: NodeV1, options: ClientOptions = ClientOptions()) -> NodeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    return patch(client, metamart_type.spec, options)


@patch.register
def patch_node_spec(client: ClientV1, metamart_type: NodeSpec, options: ClientOptions = ClientOptions()) -> NodeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    if metamart_type.id is None:
        current = get(client, metamart_type)
        metamart_type.id = current.spec.id
    url = f"{client.get_url(metamart_type)}{metamart_type.id}/"
    response = patch(client, url, metamart_type.dict(exclude_none=True), options=options).json()
    return NodeV1.from_spec(response)


@patch.register
def patch_edge_v1(client: ClientV1, metamart_type: EdgeV1, options: ClientOptions = ClientOptions()) -> NodeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    return patch(client, metamart_type.spec, options)


@patch.register
def patch_edge_spec(client: ClientV1, metamart_type: EdgeSpec, options: ClientOptions = ClientOptions()) -> EdgeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    if metamart_type.id is None:
        current = get(client, metamart_type)
        metamart_type.id = current.spec.id

    payload = metamart_type.dict(exclude_none=True)

    url = f"{client.get_url(metamart_type)}{metamart_type.id}/"
    response = patch(client, url, payload, options=options)
    response = response.json()

    response["source"] = {**payload["source"], "id": response["source"]}
    response["destination"] = {**payload["destination"], "id": response["destination"]}
    return EdgeV1.from_spec(response)


@patch.register
def patch_sourced_node_v1(
    client: ClientV1, metamart_type: SourcedNodeV1, options: ClientOptions = ClientOptions()
) -> SourcedNodeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """

    return patch(client, metamart_type.spec, options)


@patch.register
def patch_sourced_node_spec(
    client: ClientV1, metamart_type: SourcedNodeSpec, options: ClientOptions = ClientOptions()
) -> SourcedNodeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    source, node = get_source_and_spec(client, metamart_type)

    url = client.get_url(metamart_type, source.id, node.id)
    response = patch(client, url, metamart_type.dict(exclude_none=True), options=options).json()
    response["data_source"] = source
    return SourcedNodeV1.from_spec(response)


@patch.register
def patch_sourced_edge_v1(
    client: ClientV1, metamart_type: SourcedEdgeV1, options: ClientOptions = ClientOptions()
) -> SourcedEdgeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """

    return patch(client, metamart_type.spec, options)


@patch.register
def patch_sourced_edge_spec(
    client: ClientV1, metamart_type: SourcedEdgeSpec, options: ClientOptions = ClientOptions()
) -> SourcedEdgeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    source, node = get_source_and_spec(client, metamart_type)

    url = client.get_url(metamart_type, source.id, node.id)
    payload = metamart_type.dict(exclude_none=True)

    response = patch(client, url, payload, options=options).json()
    response.update(
        {
            "data_source": source,
            "source": {**payload["source"], "id": response["source"]},
            "destination": {**payload["destination"], "id": response["destination"]},
        }
    )

    return SourcedEdgeV1.from_spec(response)


@patch.register
def patch_workspace_v1(
    client: ClientV1, metamart_type: Union[WorkspaceV1, WorkspaceSpec], options: ClientOptions = ClientOptions()
):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    message = "The patch workspace endpoint is not supported through the REST API."
    raise NotSupportedError(message)


@patch.register
def patch_organisation_v1(
    client: ClientV1, metamart_type: Union[OrganisationV1, OrganisationSpec], options: ClientOptions = ClientOptions()
):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    message = "The patch organisation endpoint is not supported through the REST API."
    raise NotSupportedError(message)


@patch.register
def patch_source_v1(client: ClientV1, metamart_type: SourceV1, options: ClientOptions = ClientOptions()) -> SourceV1:
    """

    Args:
        client (ClientV1):
        metamart_type (NodeV1):
        options (ClientOptions, optional):  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    return patch(client, metamart_type.spec, options)


@patch.register
def patch_source_spec(client: ClientV1, metamart_type: SourceSpec, options: ClientOptions = ClientOptions()) -> SourceV1:
    """

    Args:
        client (ClientV1):
        metamart_type (NodeV1):
        options (ClientOptions, optional):  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    if metamart_type.id is None:
        current = get(client, metamart_type)
        metamart_type.id = current.spec.id

    url = f"{client.get_url(metamart_type)}{metamart_type.id}/"

    response = patch(client, url, metamart_type.dict(exclude_none=True), options=options)
    response = response.json()
    response["workspace"] = client.workspace
    return SourceV1.from_spec(response)
