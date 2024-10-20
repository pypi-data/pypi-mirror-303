from typing import Union

from metamart_schemas.v1 import OrganisationV1
from metamart_schemas.v1.organization import OrganisationSpec

from metamart_client.endpoints.client import ClientOptions
from metamart_client.endpoints.rest import get
from metamart_client.endpoints.v1.client import ClientV1
from metamart_client.errors import NotSupportedError
from metamart_client.schemas.labels import OrganisationLabels


@get.register
def get_organisation_v1(
    client: ClientV1,
    metamart_type: OrganisationLabels,
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
    message = "The get organisation endpoint is not supported through the REST API."
    raise NotSupportedError(message)


@get.register
def get_organisation_v1(
    client: ClientV1,
    metamart_type: Union[OrganisationV1, OrganisationSpec],
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
    message = "The get organisation endpoint is not supported through the REST API."
    raise NotSupportedError(message)
