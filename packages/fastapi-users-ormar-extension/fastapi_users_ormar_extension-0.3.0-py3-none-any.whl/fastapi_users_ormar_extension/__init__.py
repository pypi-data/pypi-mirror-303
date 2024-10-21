"""Use ormar as ORM in your fastapi-users."""
import uuid
from typing import Any, Dict, Generic, Optional, Type

import ormar
from fastapi_users.db.base import BaseUserDatabase
from fastapi_users.models import ID, UP, OAP

UUID_ID = uuid.UUID


class OrmarBaseUserTable(Generic[ID]):
    email: str = ormar.String(max_length=320, unique=True, index=True, nullable=False)
    hashed_password: str = ormar.String(max_length=1024, nullable=False)
    is_active: bool = ormar.Boolean(default=True, nullable=False)
    is_superuser: bool = ormar.Boolean(default=False, nullable=False)
    is_verified: bool = ormar.Boolean(default=False, nullable=False)


class OrmarBaseUserTableUUID(ormar.Model, OrmarBaseUserTable[UUID_ID]):
    ormar_config = ormar.OrmarConfig(
        tablename="users",
        abstract=True,
    )

    id: UUID_ID = ormar.UUID(primary_key=True, default=uuid.uuid4, uuid_format="string")


class OrmarBaseOAuthAccountTable(Generic[ID]):
    oauth_name: str = ormar.String(max_length=100, index=True, nullable=False)
    access_token: str = ormar.String(max_length=1024, nullable=False)
    expires_at: Optional[int] = ormar.Integer(nullable=False)
    refresh_token: Optional[int] = ormar.String(max_length=1024, nullable=True)
    account_id: str = ormar.String(max_length=320, index=True, nullable=False)
    account_email: str = ormar.String(max_length=320, nullable=False)


class OrmarBaseOAuthAccountTableUUID(ormar.Model, OrmarBaseOAuthAccountTable[UUID_ID]):
    ormar_config = ormar.OrmarConfig(
        tablename="oauth_accounts",
        abstract=True,
    )

    id: UUID_ID = ormar.UUID(primary_key=True, default=uuid.uuid4, uuid_format="string")

    # When subclassing, define
    # user: User = ormar.ForeignKey(User, nullable=False, ondelete="cascade")


class OrmarUserDatabase(Generic[UP, ID], BaseUserDatabase[UP, ID]):
    user_table: Type[UP]
    oauth_account_table: Optional[Type[OrmarBaseOAuthAccountTable]]

    def __init__(
            self,
            user_table: Type[UP],
            oauth_account_table: Optional[Type[OrmarBaseOAuthAccountTable]] = None,
    ):
        self.user_table = user_table
        self.oauth_account_table = oauth_account_table

    async def get(self, id: ID) -> Optional[UP]:
        return await self.user_table.objects.get_or_none(id=id)

    async def get_by_email(self, email: str) -> Optional[UP]:
        return await self.user_table.objects.get_or_none(email=email)

    async def get_by_oauth_account(self, oauth: str, account_id: str) -> Optional[UP]:
        if self.oauth_account_table is None:
            raise NotImplementedError()

        return await self.user_table.objects.prefetch_related(
            "oauth_accounts"
        ).get_or_none(
            oauth_accounts__oauth_name=oauth, oauth_accounts__account_id=account_id
        )

    async def create(self, create_dict: Dict[str, Any]) -> UP:
        return await self.user_table.objects.create(**create_dict)

    async def update(self, user: UP, update_dict) -> UP:
        for key, value in update_dict.items():
            setattr(user, key, value)
        await user.update()
        return user

    async def delete(self, user: UP) -> None:
        await user.delete()

    async def add_oauth_account(self, user: UP, create_dict: Dict[str, Any]):
        if self.oauth_account_table is None:
            raise NotImplementedError()

        oauth_account = await self.oauth_account_table.objects.create(
            **create_dict, user=user
        )
        await user.load()
        return user

    async def update_oauth_account(
            self, user: UP, oauth_account: OAP, update_dict: Dict[str, Any]
    ) -> UP:
        for key, value in update_dict.items():
            setattr(oauth_account, key, value)

        await oauth_account.update()
        return user
