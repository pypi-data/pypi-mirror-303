import os
from pathlib import Path

import requests
from loguru import logger


def create_aws_web_identity_token_if_required() -> None:
    """Creates a GCP OIDC token if `AWS_WEB_IDENTITY_TOKEN_FILE` is set

    The GCP OIDC token is then used to impersonate the corresponding AWS IAM role. We're
    only using this mechanism when running within GCP. For local development, we're
    using standard AWS credentials.

    Being inside GCP is identified by the presence of the `AWS_WEB_IDENTITY_TOKEN_FILE`
    environment variable.

    """
    token_file = os.getenv("AWS_WEB_IDENTITY_TOKEN_FILE")
    if token_file is None:
        logger.debug(
            "No token file specified by the AWS_WEB_IDENTITY_TOKEN_FILE environment "
            "variable, not attempting to create a GCP OIDC token. This is expected in "
            "local development."
        )
        return

    # Writing a token file has no point if `AWS_ARN_ROLE` is not set
    role_arn = os.getenv("AWS_ROLE_ARN")
    if role_arn is None:
        raise ValueError("AWS_ROLE_ARN not set, but AWS_WEB_IDENTITY_TOKEN_FILE is set")

    headers = {"Metadata-Flavor": "Google"}
    # This call will only work when running within GCP
    response = requests.get(
        "http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=sts.amazonaws.com",
        headers=headers,
    )
    response.raise_for_status()
    token = response.text

    if token is None or token == "":
        raise ValueError("Returned OIDC token seems to be empty")

    logger.debug(f"Writing OIDC token to {token_file}")
    with Path(token_file).open("w") as f:
        f.write(token)
