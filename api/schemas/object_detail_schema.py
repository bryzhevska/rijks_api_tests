from typing import Optional

from pydantic import BaseModel


class ArtObjectDetail(BaseModel):
    title: str
    principalMaker: str
    description: Optional[str]


class ObjectDetailResponse(BaseModel):
    artObject: ArtObjectDetail
