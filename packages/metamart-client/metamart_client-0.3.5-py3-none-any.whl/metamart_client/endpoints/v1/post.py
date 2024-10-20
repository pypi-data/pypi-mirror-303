from typing import Dict, List, Optional, Union
from uuid import UUID

from metamart_schemas.v1 import EdgeV1, NodeV1, WorkspaceV1
from metamart_schemas.v1.edge import EdgeSpec, SourcedEdgeSpec, SourcedEdgeV1
from metamart_schemas.v1.node import NodeSpec, SourcedNodeSpec, SourcedNodeV1
from metamart_schemas.v1.organization import OrganisationSpec, OrganisationV1
from metamart_schemas.v1.source import SourceSpec, SourceV1
from metamart_schemas.v1.workspace import WorkspaceSpec

from metamart_client.endpoints.client import ClientOptions
from metamart_client.endpoints.rest import get, post
from metamart_client.endpoints.v1.client import ClientV1
from metamart_client.endpoints.v1.utils import process_node_id
from metamart_client.errors import NotSupportedError


def collect_data_sources(data_sources: List[Union[UUID, SourceSpec]]) -> List[Union[Dict, SourceSpec]]:
    """

    Args:
        data_sources:

    Returns:

    Raises:

    """
    result = []
    for source in data_sources:
        if isinstance(source, UUID):
            source_obj = {"id": source}
        elif isinstance(source, SourceSpec):
            source_obj = {"id": source.id} if source.id else {"name": source.name}
        else:
            raise NotSupportedError(f"Only UUIDs and SourceSpecs are supported not {type(source)}")

        result.append(source_obj)

    return result


@post.register
def post_node_by_node_v1(client: ClientV1, metamart_type: NodeV1, options: ClientOptions = ClientOptions()) -> NodeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    return post(client, metamart_type.spec, options)


@post.register
def post_node_by_spec(client: ClientV1, metamart_type: NodeSpec, options: ClientOptions = ClientOptions()) -> NodeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    url = client.get_url(metamart_type)
    payload = metamart_type.dict(exclude_none=True)
    payload["data_sources"] = collect_data_sources(metamart_type.data_sources)
    response = post(client, url, payload, options)

    return NodeV1.from_spec(response.json())


@post.register
def post_sourced_node_v1(
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
    return post(client, metamart_type.spec, options)


@post.register
def post_sourced_node_spec(
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
    source_spec = metamart_type.data_source
    if (source_id := source_spec.id) is None:
        source_spec = get(client, source_spec).spec
        source_id = source_spec.id

    url = client.get_url("SourceNode", source_id)
    response = post(client, url, metamart_type.dict(exclude_none=True), options=options).json()
    response["data_source"] = source_spec
    return SourcedNodeV1.from_spec(response)


@post.register
def post_sourced_edge_v1(
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
    return post(client, metamart_type.spec, options)


@post.register
def post_sourced_edge_spec(
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
    source_spec = metamart_type.data_source
    if (source_id := source_spec.id) is None:
        source_spec = get(client, source_spec).spec
        source_id = source_spec.id

    url = client.get_url("SourceEdge", source_id)
    payload = metamart_type.dict(exclude_none=True)

    response = post(client, url, payload, options=options).json()

    response.update(
        {
            "data_source": source_spec,
            "source": {**payload["source"], "id": response["source"]},
            "destination": {**payload["destination"], "id": response["destination"]},
        }
    )

    return SourcedEdgeV1.from_spec(response)


@post.register
def post_edge_by_spec(client: ClientV1, metamart_type: EdgeSpec, options: ClientOptions = ClientOptions()) -> EdgeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    url = client.get_url(metamart_type)

    payload = metamart_type.dict(exclude_none=True)
    payload["data_sources"] = collect_data_sources(metamart_type.data_sources)

    response = post(client, url, payload, options=options)
    response = response.json()

    response["source"] = {**payload["source"], "id": response["source"]}
    response["destination"] = {**payload["destination"], "id": response["destination"]}

    return EdgeV1.from_spec(response)


@post.register
def post_edge_by_edge_v1(client: ClientV1, metamart_type: EdgeV1, options: ClientOptions = ClientOptions()) -> EdgeV1:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    return post(client, metamart_type.spec, options)


@post.register
def post_workspace_v1(
    client: ClientV1, metamart_type: Union[WorkspaceV1, WorkspaceSpec], options: ClientOptions = ClientOptions()
) -> WorkspaceV1:
    """
    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:
    """
    spec = metamart_type.spec if isinstance(metamart_type, WorkspaceV1) else metamart_type
    url = client.get_url(metamart_type)
    payload = spec.dict(exclude_none=True)

    if isinstance(spec.organisation, UUID):
        organisation_id = metamart_type.spec.organisation
    elif isinstance(spec.organisation, OrganisationSpec) and spec.organisation.id is not None:
        organisation_id = spec.organisation.id
    else:
        error_message = (
            f"An attempt was made to post the workspace `{spec.ref}`. Unfortunately, no Organisation id was"
            f"provided as part of the request and the client library does not currently support posting a workspace "
            f"without an organisation id."
        )
        raise ValueError(error_message)

    payload["organisation"] = organisation_id

    response = post(client, url, payload, options=options)
    return WorkspaceV1.from_spec(response.json())


@post.register
def post_source_v1(client: ClientV1, metamart_type: SourceSpec, options: ClientOptions = ClientOptions()) -> SourceV1:
    """
    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:
    """
    url = client.get_url(metamart_type)

    if metamart_type.workspace_id is not None:
        if client.workspace != str(metamart_type.workspace_id):
            message = (
                f"The workspace id provided in the source {metamart_type} does not match the client's "
                f"workspace id {client.workspace}."
            )
            raise ValueError(message)

    payload = metamart_type.dict(exclude_none=True)
    payload.pop("workspace", None)

    response = post(client, url, payload, options=options).json()
    response["workspace"] = client.workspace
    return SourceV1.from_spec(response)


@post.register
def post_source_v1(client: ClientV1, metamart_type: SourceV1, options: ClientOptions = ClientOptions()) -> SourceV1:
    """
    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:
    """
    return post(client, metamart_type.spec, options)


@post.register
def post_organisation_v1(
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
    message = "The post organisation endpoint is not supported through the REST API."
    raise NotSupportedError(message)
