from typing import Union

from metamart_schemas.v1 import EdgeV1, NodeV1, SourcedNodeV1, SourceV1
from metamart_schemas.v1.edge import SourcedEdgeSpec, SourcedEdgeV1
from metamart_schemas.v1.node import SourcedNodeSpec
from metamart_schemas.v1.organization import OrganisationSpec, OrganisationV1
from metamart_schemas.v1.workspace import WorkspaceSpec, WorkspaceV1

from metamart_client.endpoints.client import ClientOptions
from metamart_client.endpoints.rest import delete, get
from metamart_client.endpoints.v1.client import ClientV1
from metamart_client.endpoints.v1.get.utils import get_source_and_spec
from metamart_client.errors import NotSupportedError
from metamart_client.schemas.labels import (
    EdgeLabels,
    NodeLabels,
    OrganisationLabels,
    SourceEdgeLabels,
    SourceLabels,
    SourceNodeLabels,
    WorkspaceLabels,
)


@delete.register
def delete_node_v1(client: ClientV1, metamart_type: NodeV1, options: ClientOptions = ClientOptions()):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    if metamart_type.spec.id is None:
        metamart_type = get(client, metamart_type)
        if metamart_type is None:
            return
    url = f"{client.get_url(metamart_type)}{metamart_type.spec.id}/"
    delete(client, url, options=options)


@delete.register
def delete_source_node_by_source_node_v1(
    client: ClientV1, metamart_type: SourcedNodeV1, options: ClientOptions = ClientOptions()
):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    delete(client, metamart_type.spec, options)


@delete.register
def delete_source_node_spec(client: ClientV1, metamart_type: SourcedNodeSpec, options: ClientOptions = ClientOptions()):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """

    source, node = get_source_and_spec(client, metamart_type)
    url = client.get_url("SourceNode", source.id, node.id)
    delete(client, url, options=options)


@delete.register
def delete_source_edge_by_source_node_v1(
    client: ClientV1, metamart_type: SourcedEdgeV1, options: ClientOptions = ClientOptions()
):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    delete(client, metamart_type.spec, options)


@delete.register
def delete_source_edge_spec(client: ClientV1, metamart_type: SourcedEdgeSpec, options: ClientOptions = ClientOptions()):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    source, node = get_source_and_spec(client, metamart_type)
    url = client.get_url("SourceEdge", source.id, node.id)
    delete(client, url, options=options)


@delete.register
def delete_edge_v1(client: ClientV1, metamart_type: EdgeV1, options: ClientOptions = ClientOptions()):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    if metamart_type.spec.id is None:
        metamart_type = get(client, metamart_type)
        if metamart_type is None:
            return
    url = f"{client.get_url(metamart_type)}{metamart_type.spec.id}/"
    delete(client, url, options=options)


@delete.register
def delete_workspace_v1(
    client: ClientV1,
    metamart_type: Union[WorkspaceV1, WorkspaceSpec, WorkspaceLabels],
    options: ClientOptions = ClientOptions(),
):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    message = (
        "The delete workspace endpoint is not supported through the REST API. If you wish to delete a workspace, "
        "please contact support or use the admin interface."
    )
    raise NotSupportedError(message)


@delete.register
def delete_organisation_v1(
    client: ClientV1,
    metamart_type: Union[OrganisationV1, OrganisationSpec, OrganisationLabels],
    options: ClientOptions = ClientOptions(),
):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    message = "The delete organisation endpoint is not supported through the REST API."
    raise NotSupportedError(message)


@delete.register
def delete_source_by_label(client: ClientV1, metamart_type: SourceLabels, options: ClientOptions = ClientOptions()):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    message = (
        "It's not possible to delete all sources through the REST API. If you really wish to delete all sources, "
        "You must do so iteratively through each individual source"
    )
    raise NotSupportedError(message)


@delete.register
def delete_source_by_source_v1(client: ClientV1, metamart_type: SourceV1, options: ClientOptions = ClientOptions()):
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    if metamart_type.spec.id is None:
        metamart_type = get(client, metamart_type)
        if metamart_type is None:
            return
    url = f"{client.get_url(metamart_type)}{metamart_type.spec.id}/"
    delete(client, url, options=options)
