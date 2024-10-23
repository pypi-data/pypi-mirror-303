from abc import ABC, abstractmethod

from connector.async_.abstract import AbstractCommands
from connector.serializers.lumos import (
    ActivateAccountArgsBase,
    ActivateAccountResp,
    AssignEntitlementArgsBase,
    AssignEntitlementResp,
    CreateAccountArgsBase,
    CreateAccountResp,
    DeactivateAccountArgsBase,
    DeactivateAccountResp,
    DeleteAccountArgsBase,
    DeleteAccountResp,
    FindEntitlementAssociationsArgsBase,
    FindEntitlementAssociationsResp,
    GetLastActivityArgsBase,
    GetLastActivityResp,
    ListAccountsArgsBase,
    ListAccountsResp,
    ListCustomAttributesSchemaArgsBase,
    ListCustomAttributesSchemaResp,
    ListEntitlementsArgsBase,
    ListEntitlementsResp,
    ListResourcesArgsBase,
    ListResourcesResp,
    UnassignEntitlementArgsBase,
    UnassignEntitlementResp,
    ValidateCredentialsArgsBase,
    ValidateCredentialsResp,
)

__all__ = ("LumosCommandsMixin",)


class LumosCommandsMixin(AbstractCommands, ABC):
    @abstractmethod
    async def list_accounts(self, args: ListAccountsArgsBase) -> ListAccountsResp:
        """
        List a page of accounts.
        """
        raise NotImplementedError

    @abstractmethod
    async def validate_credentials(
        self, args: ValidateCredentialsArgsBase
    ) -> ValidateCredentialsResp:
        """
        Validate that given credentials can be used for base
        integration capabilities.
        """
        raise NotImplementedError

    @abstractmethod
    async def list_resources(self, args: ListResourcesArgsBase) -> ListResourcesResp:
        """
        Fetches a list of resources of the given types.
        """
        raise NotImplementedError

    @abstractmethod
    async def list_entitlements(
        self,
        args: ListEntitlementsArgsBase,
    ) -> ListEntitlementsResp:
        """
        Fetches a list of entitlements for each of the resources. Both
        directly assignable and unassignable to accounts.
        """
        raise NotImplementedError

    @abstractmethod
    async def find_entitlement_associations(
        self, args: FindEntitlementAssociationsArgsBase
    ) -> FindEntitlementAssociationsResp:
        """
        Finds associations between accounts and entitlements,
        which are tied to resources.
        """
        raise NotImplementedError

    @abstractmethod
    async def assign_entitlement(self, args: AssignEntitlementArgsBase) -> AssignEntitlementResp:
        """
        Assigns an account directly to an entitlement.

        Requires that the account, resource & entitlement exist
        in the third party application.
        """
        raise NotImplementedError

    @abstractmethod
    async def unassign_entitlement(
        self, args: UnassignEntitlementArgsBase
    ) -> UnassignEntitlementResp:
        """
        Unassigns an account directly from an entitlement.

        Requires that the account, resource & entitlement exist
        in the third party application.
        """
        raise NotImplementedError

    @abstractmethod
    async def list_custom_attributes_schema(
        self, args: ListCustomAttributesSchemaArgsBase
    ) -> ListCustomAttributesSchemaResp:
        """
        Finds the schema to use for custom attributes.
        """
        raise NotImplementedError

    @abstractmethod
    async def create_account(self, args: CreateAccountArgsBase) -> CreateAccountResp:
        """
        Creates a new account.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete_account(self, args: DeleteAccountArgsBase) -> DeleteAccountResp:
        """
        Deletes an account.
        """
        raise NotImplementedError

    @abstractmethod
    async def activate_account(self, args: ActivateAccountArgsBase) -> ActivateAccountResp:
        """
        Activates an account.
        """
        raise NotImplementedError

    @abstractmethod
    async def deactivate_account(self, args: DeactivateAccountArgsBase) -> DeactivateAccountResp:
        """
        Deactivates an account.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_last_activity(self, args: GetLastActivityArgsBase) -> GetLastActivityResp:
        """
        Returns the last activity of specified users.
        """
        raise NotImplementedError
