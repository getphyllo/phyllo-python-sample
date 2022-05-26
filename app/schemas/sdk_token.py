from __future__ import annotations

from typing import List

from pydantic import BaseModel


class SdkToken(BaseModel):
    user_id: str
    products: List[str]


class SdkTokenRequest(SdkToken):
    pass
