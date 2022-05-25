from __future__ import annotations

from pydantic import BaseModel, constr


class UserBase(BaseModel):
    name: constr(min_length=1, strip_whitespace=True)  # type: ignore
    external_id: constr(min_length=1, strip_whitespace=True)  # type: ignore


class UserRequest(UserBase):
    pass
