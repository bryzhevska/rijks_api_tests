from typing import List

from pydantic import BaseModel, HttpUrl


class Image(BaseModel):
    guid: str
    offsetPercentageX: int
    offsetPercentageY: int
    width: int
    height: int
    url: HttpUrl


class ArtObject(BaseModel):
    links: dict
    id: str
    objectNumber: str
    title: str
    hasImage: bool
    principalOrFirstMaker: str
    longTitle: str
    showImage: bool
    permitDownload: bool
    webImage: Image
    headerImage: Image
    productionPlaces: List[str]


class CollectionResponse(BaseModel):
    elapsedMilliseconds: int
    count: int
    artObjects: List[ArtObject]
