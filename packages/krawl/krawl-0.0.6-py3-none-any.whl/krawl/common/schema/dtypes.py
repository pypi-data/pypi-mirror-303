from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class TagEnum(str, Enum):
    class_ = "class"
    href = "href"
    url = "a"
    id_ = "id"


class HTMLNodeContext(BaseModel):
    tag: str
    classname: str
    idname: str
    wordcount: int
    href: str = ""


class CrawlResponse(BaseModel):
    first: str
    items: List[str]


class HtmlFlagEnum(str, Enum):
    A00 = "Normal"
    B00 = "Only readable via emulated browser"
    B01 = "B00, but blocking due to cookies"
    E00 = "Not readable at all"


class Href(BaseModel):
    text: str
    url: str


class StructuredResponse(BaseModel):
    title: str
    coretext: str
    text: str = Field('', description="Fulltext")
    h1: List[str] = Field(default_factory=list)
    h2: List[str] = Field(default_factory=list)
    links: List[Href] = Field(default_factory=list)
    ilinks: List[Href] = Field(default_factory=list)
    olinks: List[Href] = Field(default_factory=list)
    image_url_primary: str = Field('', description="URL of the primary image")
    origin: str = Field('', description="Original url")
    status: HtmlFlagEnum = HtmlFlagEnum.A00


class StructuredResponseGroup(BaseModel):
    first: StructuredResponse
    items: List[StructuredResponse]
