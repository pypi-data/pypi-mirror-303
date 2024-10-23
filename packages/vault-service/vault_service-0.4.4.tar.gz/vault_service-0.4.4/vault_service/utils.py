from vault_service.models.response import Response
from vault_service.models.model import SecretData
from vault_service.services.vault_controller import VaultController
import hvac


def store_secret(service_id: str, tenant_id: str, secret_name: str, secret_data: SecretData):
    try:
        vault_controller = VaultController()
        if vault_controller is None:
            return Response(status="error", message="VaultController not initialized").dict()
        vault_controller.store_secret(service_id, tenant_id, secret_name, secret_data)
        return Response(status="success" , message= "Secret stored successfully").dict()
    except Exception as e:
        return Response(status="error", message=f"Error in store_secret with exception {e}").dict()

def get_secret(service_id: str, tenant_id: str, secret_name: str):
    try:
        vault_controller = VaultController()
        if vault_controller is None:
            return Response(status="error", message="VaultController not initialized").dict()
        secret = vault_controller.get_secret(service_id, tenant_id, secret_name)
        if secret is None:
            return Response(status="error", message="Secret not found").dict()
        return Response(status="success" , message= "Secret fetched successfully", data=secret).dict()
    except hvac.exceptions.Forbidden:
        return Response(status="error", message="Vault Server permission denied").dict()
    except hvac.exceptions.VaultError as e:
        return Response(status="error", message="Secret not found").dict()
    except ValueError as e:
        return Response(status="error", message=f"{e}").dict()
    except Exception as e:
        return Response(status="error", message=f"Error in get_secret with exception {e}").dict()

def update_secret(service_id: str, tenant_id: str, secret_name: str, secret_data: SecretData):
    try:
        vault_controller = VaultController()
        if vault_controller is None:
            return Response(status="error", message="VaultController not initialized").dict()
        resp_dict = vault_controller.update_secret(service_id, tenant_id, secret_name, secret_data)
        if "status" in resp_dict:
            return Response(status="error", message=resp_dict["message"]).dict()
        return Response(status="success", message="Secret updated successfully").dict()
    except Exception as e:
        return Response(status="error", message=f"Error in update_secret with exception {e}").dict()

def delete_secret(service_id: str, tenant_id: str, secret_name: str):
    try:
        vault_controller = VaultController()
        if vault_controller is None:
            return Response(status="error", message="VaultController not initialized").dict()
        resp_dict = vault_controller.delete_secret(service_id, tenant_id, secret_name)
        if "status" in resp_dict:
            return Response(status="error", message=resp_dict["message"]).dict()
        return Response(status="success", message="Secret deleted successfully").dict()
    except Exception as e:
        return Response(status="error", message=f"Error in delete_secret with exception {e}").dict()

def get_all_secrets_for_tenant(service_id: str, tenant_id: str):
    try:
        vault_controller = VaultController()
        if vault_controller is None:
            return Response(status="error", message="VaultController not initialized").dict()
        secrets = vault_controller.get_all_secrets_for_tenant(service_id, tenant_id)
        return Response(status="success" , message= "Secret fetched successfully", data=secrets).dict()
    except Exception as e:
        return Response(status="error", message=f"Error in get_all_secrets_for_tenant with exception {e}").dict()

def delete_all_secrets_for_tenant(service_id: str, tenant_id: str):
    try:
        vault_controller = VaultController()
        if vault_controller is None:
            return Response(status="error", message="VaultController not initialized").dict()
        vault_controller.delete_all_secrets_for_tenant(service_id, tenant_id)
        return Response(status="success", message="All secrets for tenant deleted successfully").dict()
    except Exception as e:
        return Response(status="error", message=f"Error in delete_all_secrets_for_tenant with exception {e}").dict()
