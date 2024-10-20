from typing import List, Optional, Union
from uuid import UUID

from metamart_schemas.v1 import WorkspaceV1
from metamart_schemas.v1.workspace import WorkspaceSpec
from httpx import Response

from metamart_client.endpoints.client import ClientOptions
from metamart_client.endpoints.rest import get, get_is_unique, paginated_get
from metamart_client.endpoints.utilities import (
    add_query_params,
    expects_unique_query,
    is_valid_uuid,
    paginated,
    response_status_check,
)
from metamart_client.endpoints.v1.client import ClientV1
from metamart_client.errors import InvalidResponseError, ObjectNotFoundError
from metamart_client.schemas.labels import WorkspaceLabels


def get_workspace_by_url(
    client: ClientV1,
    url: str,
    options: ClientOptions = ClientOptions(),
) -> Response:
    """

    Args:
        client:
        metamart_type:
        url:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    query_args = {"workspace": client.workspace, **options.query_args}
    url = add_query_params(url, query_args)

    response = client.session.get(url, headers=options.headers, **options.request_args)
    response_status_check(response)
    return response


get_workspace_by_paginated_url = paginated(get_workspace_by_url)


@get.register
def get_all_workspaces(
    client: ClientV1,
    metamart_type: WorkspaceLabels,
    options: ClientOptions = ClientOptions(),
) -> List[WorkspaceV1]:
    """

    Args:
        client:
        metamart_type:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    resp = get_workspace_by_paginated_url(client, client.get_url(metamart_type), options)
    return [WorkspaceV1.from_spec(item) for item in resp]


@get.register
def get_workspace_by_uuid(
    client: ClientV1,
    metamart_type: WorkspaceLabels,
    workspace_id: Union[UUID, str],
    options: ClientOptions = ClientOptions(),
) -> WorkspaceV1:
    """

    Args:
        client:
        metamart_type:
        workspace_id:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    url = client.get_url(metamart_type)
    if not is_valid_uuid(workspace_id):
        message = f"The provided workspace id {workspace_id} is not a valid uuid."
        raise ValueError(message)
    url = f"{url}{workspace_id}/"
    result = get_workspace_by_url(client, url, options=options)
    return WorkspaceV1.from_spec(result.json())


@get.register
def get_workspace_by_workspace_v1(
    client: ClientV1,
    metamart_type: WorkspaceV1,
    options: ClientOptions = ClientOptions(),
) -> WorkspaceV1:
    """

    Args:
        client:
        metamart_type:
        name:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    return get(client, metamart_type.spec, options=options)


@get.register
def get_workspace_by_spec(
    client: ClientV1,
    metamart_type: WorkspaceSpec,
    options: ClientOptions = ClientOptions(),
) -> WorkspaceV1:
    """

    Args:
        client:
        metamart_type:
        name:
        options:  (Default value = ClientOptions())

    Returns:

    Raises:

    """
    if metamart_type.id is not None:
        return get(client, "Workspace", metamart_type.id, options=options)

    options = options.copy()
    options.query_args["ref"] = metamart_type.ref
    resp = get_workspace_by_paginated_url(client, client.get_url(metamart_type), options)

    if len(resp) == 1:
        return WorkspaceV1.from_spec(resp[0])
    elif len(resp) == 0:
        raise ObjectNotFoundError(f"Could not find a workspace with ref {metamart_type.ref}")
    else:
        raise InvalidResponseError(
            f"Found more than one workspace with ref {metamart_type.ref}. This should not happen. "
            f"Please create an issue at www.github.com/meta-mart/metamart-core/issues"
        )
