from dataclasses import asdict

import requests

from automizor.exceptions import AutomizorError, NotFound
from automizor.utils import get_api_config, get_headers

from ._container import SecretContainer


class Vault:
    """
    `Vault` is a secure storage class within the `Automizor Platform` for managing
    secrets such as API keys, passwords, and other sensitive information. It offers
    functionality to securely retrieve and update secrets through direct interaction
    with the `Automizor API`.

    Configuration for accessing and manipulating these secrets is driven by environment
    variables, which are essential for specifying the API's host and token for
    authentication purposes.

    Environment variables requisite for operation include:
    - ``AUTOMIZOR_AGENT_TOKEN``: The token for authenticating against the `Automizor API`.

    Example usage:

    .. code-block:: python

        from automizor import vault

        # Create a new secret
        vault.create_secret(name="MySecret", value={"username": "admin", "password": "*****"})

        # Retrieve a secret by its name
        secret = vault.get_secret("MySecret")
        print(secret.get("username"))  # Output: "admin"
        print(secret.get("password"))  # Output: "*****"

        # Update a existing secret
        secret = vault.get_secret("MySecret")
        secret.update({"username": "user"})
        vault.set_secret(secret)
    """

    _instance = None

    @classmethod
    def configure(cls, api_token: str | None = None):
        cls._instance = cls(api_token)

    def __init__(self, api_token: str | None = None):
        self.url, self.token = get_api_config(api_token)
        self.session = requests.Session()
        self.session.headers.update(get_headers(self.token))

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls.configure()
        return cls._instance

    def create_secret(self, secret: SecretContainer) -> SecretContainer:
        """
        Creates a new secret. Stores the secret in the `Automizor API`.
        If the secret already exists, it will be updated.

        Args:
            secret: The secret to create.

        Returns:
            The created secret.

        Raises:
            AutomizorVaultError: If creating the secret fails.
        """

        try:
            return self._update_secret(secret)
        except NotFound:
            return self._create_secret(secret)

    def get_secret(self, name) -> SecretContainer:
        """
        Retrieves a secret by its name. Fetches from the `Automizor API`.

        Args:
            name: The name of the secret to retrieve.

        Returns:
            The retrieved secret.

        Raises:
            AutomizorVaultError: If retrieving the secret fails.
        """

        return self._get_secret(name)

    def set_secret(self, secret: SecretContainer) -> SecretContainer:
        """
        Updates an existing secret. Updates to the `Automizor API`.

        Args:
            secret: The secret to update.

        Returns:
            The updated secret.

        Raises:
            AutomizorVaultError: If updating the secret fails.
        """

        return self._update_secret(secret)

    def _create_secret(self, secret: SecretContainer) -> SecretContainer:
        url = f"https://{self.url}/api/v1/vault/secret/"
        try:
            response = self.session.post(url, timeout=10, json=asdict(secret))
            response.raise_for_status()
            return SecretContainer(**response.json())
        except requests.HTTPError as exc:
            raise AutomizorError.from_response(
                exc.response, "Failed to create secret"
            ) from exc
        except Exception as exc:
            raise AutomizorError(f"Failed to create secret: {exc}") from exc

    def _get_secret(self, name: str) -> SecretContainer:
        url = f"https://{self.url}/api/v1/vault/secret/{name}/"
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return SecretContainer(**response.json())
        except requests.HTTPError as exc:
            raise AutomizorError.from_response(
                exc.response, "Failed to get secret"
            ) from exc
        except Exception as exc:
            raise AutomizorError(f"Failed to get secret: {exc}") from exc

    def _update_secret(self, secret: SecretContainer) -> SecretContainer:
        url = f"https://{self.url}/api/v1/vault/secret/{secret.name}/"
        try:
            response = self.session.put(url, timeout=10, json=asdict(secret))
            response.raise_for_status()
            return SecretContainer(**response.json())
        except requests.HTTPError as exc:
            raise AutomizorError.from_response(
                exc.response, "Failed to update secret"
            ) from exc
        except Exception as exc:
            raise AutomizorError(f"Failed to update secret: {exc}") from exc
