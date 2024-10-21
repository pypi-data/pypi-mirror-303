# fastapi-users-ormar-extension
Extension to use ormar in fastapi-users


# Installation

To install use:
```sh
pip install fastapi-users-ormar-extension
```

# Usage

Example:

```python
from typing import Optional

import ormar

from fastapi_users_ormar_extension import (
    OrmarBaseUserTableUUID,
    OrmarBaseOAuthAccountTableUUID,
)


class BaseMeta(ormar.ModelMeta):
    """Base metadata for models."""

    database = database
    metadata = meta


class User(OrmarBaseUserTableUUID):
    class Meta(BaseMeta):
        pass

    phone: str = ormar.String(nullable=False, max_length=100)


class OAuthAccount(OrmarBaseOAuthAccountTableUUID):
    class Meta(BaseMeta):
        pass

    user: User = ormar.ForeignKey(User, nullable=False, ondelete="cascade")
```