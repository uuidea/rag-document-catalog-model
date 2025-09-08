from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = None


class Entity(ConfiguredBaseModel):
    """
    An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
    """
    pass


class Asset(Entity):
    """
    An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
    """
    distribution: Optional[List[AssetDistribution]] = Field(default=None, description="""An available distribution of the dataset.""")


class AssetDistribution(Entity):
    """
    A particular physical embodiment of an Asset, which is an example of the FRBR entity manifestation (the physical embodiment of an expression of a work).
    """
    wasDerivedFrom: Optional[List[Entity]] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""")
    wasGeneratedBy: Optional[str] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""")
    modified: str = Field(default=..., description="""Most recent date on which the resource was changed, updated or modified.""")


class MarkDownFile(AssetDistribution):
    """
    Not a meaningful class, but here for illustrative purposes. Represents the processed original document into a markdown file
    """
    wasDerivedFrom: Optional[List[Entity]] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""")
    wasGeneratedBy: Optional[str] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""")
    modified: str = Field(default=..., description="""Most recent date on which the resource was changed, updated or modified.""")


class Chunk(AssetDistribution):
    """
    Not a meaningful class, but here for illustrative purposes. Represents the small part of the markdown document.
    """
    wasDerivedFrom: Optional[List[Entity]] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""")
    wasGeneratedBy: Optional[str] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""")
    modified: str = Field(default=..., description="""Most recent date on which the resource was changed, updated or modified.""")


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Entity.model_rebuild()
Asset.model_rebuild()
AssetDistribution.model_rebuild()
MarkDownFile.model_rebuild()
Chunk.model_rebuild()

